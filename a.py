from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import *
from PyQt5.uic import loadUiType
import requests
import sys
import resources_rc
import socketio
from ui_UI import Ui_MainWindow as ui
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode, urlsafe_b64decode
import os
import sounddevice as sd
from scipy.io.wavfile import write
import pygame

base_url = "https://real-time-chat-api-v1.onrender.com"

SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    b"\xdf\xe8\xebD\xe8\x81\x00\xce\xf8C\x038i\xec\x1c{\xa8\xda}\xf1\x18\xd9)p\xc14E(\x1d\xa5v\xe9",
)


def derive_key(password: bytes, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend(),
    )
    return kdf.derive(password)


def encrypt_message(message: str, key: bytes) -> str:
    try:
        salt = os.urandom(16)
        derived_key = derive_key(key, salt)
        iv = os.urandom(16)
        cipher = Cipher(
            algorithms.AES(derived_key), modes.CFB(iv), backend=default_backend()
        )
        encryptor = cipher.encryptor()
        encrypted_message = encryptor.update(message.encode()) + encryptor.finalize()
        return urlsafe_b64encode(salt + iv + encrypted_message).decode()
    except Exception as e:
        print(f"Encryption error: {e}")
        return ""


def decrypt_message(encrypted_message: str, key: bytes) -> str:
    try:
        encrypted_message = urlsafe_b64decode(encrypted_message)
        salt = encrypted_message[:16]
        iv = encrypted_message[16:32]
        encrypted_data = encrypted_message[32:]
        derived_key = derive_key(key, salt)
        cipher = Cipher(
            algorithms.AES(derived_key), modes.CFB(iv), backend=default_backend()
        )
        decryptor = cipher.decryptor()
        decrypted_message = decryptor.update(encrypted_data) + decryptor.finalize()
        return decrypted_message.decode()
    except Exception as e:
        print(f"Decryption error: {e}")
        return ""


class MainApp(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.UI_Changes()
        self.Handle_buttons()

        self.access_token = ""
        self.username = ""

        self.sio = socketio.Client()
        self.sio.on("connect", self.on_connect)
        self.sio.on("disconnect", self.on_disconnect)
        self.sio.on("user_online", self.on_new_message)
        self.sio.on("user_ofline", self.on_new_message)
        self.sio.on("error", self.on_error)
        self.sio.on("new_message", self.on_enc_new_message)
        self.sio.on("new_audio_message", self.on_new_audio_message)

    def UI_Changes(self):
        self.tabWidget.tabBar().setVisible(False)
        self.tabWidget.setCurrentIndex(0)

    def Handle_buttons(self):
        self.toolButton_11.clicked.connect(lambda: self.tabWidget.setCurrentIndex(1))
        self.toolButton_12.clicked.connect(lambda: self.tabWidget.setCurrentIndex(0))
        self.toolButton_13.clicked.connect(lambda: self.tabWidget.setCurrentIndex(3))
        self.toolButton_10.clicked.connect(lambda: self.tabWidget.setCurrentIndex(2))
        self.login_btn.clicked.connect(self.login)
        self.signup_btn.clicked.connect(self.signup)
        self.login_toolButton_3.clicked.connect(self.update_password)
        self.toolButton_9.clicked.connect(self.send_message)
        self.record_audio_button.clicked.connect(
            self.send_audio_message
        )  # Add this line

    def on_connect(self):
        print("Connected to Socket.IO server.")

    def on_disconnect(self):
        print("Disconnected from Socket.IO server.")

    def on_error(self, error):
        QMessageBox.information(self, "Error", error)

    def on_new_message(self, message):
        self.textEdit_5.insertPlainText(message + "\n")

    def on_enc_new_message(self, message):
        decrypted_message = decrypt_message(message, SECRET_KEY)
        self.textEdit_5.insertPlainText(decrypted_message + "\n")

    def on_new_audio_message(self, audio_data):
        audio_filename = "received_audio.wav"
        with open(audio_filename, "wb") as audio_file:
            audio_file.write(base64.b64decode(audio_data))
        self.textEdit_5.insertPlainText(f"Audio message received: {audio_filename}\n")
        self.play_audio(audio_filename)

    def connect_to_server(self, token):
        server_url = base_url
        self.sio.connect(server_url, auth={"token": token}, transports=["websocket"])
        self.textEdit_5.insertPlainText(self.username + " join chat" + "\n")

    def login(self):
        username = self.lineEdit_3.text()
        password = self.lineEdit_4.text()
        json_body = {"username": username, "password": password}
        api_url = f"{base_url}/api/v1/auth/login"

        try:
            response = requests.post(api_url, json=json_body)
            response.raise_for_status()
            response_json = response.json()
            user_data = response_json.get("data", {})
            self.access_token = user_data.get("accessToken")
            self.username = user_data.get("username")
            self.connect_to_server(self.access_token)
            self.tabWidget.setCurrentIndex(3)
            QMessageBox.information(self, "Login Successful", "Login was successful.")
        except requests.RequestException as e:
            error_message = (
                response.json().get("error", {}).get("message", "Unknown error")
            )
            QMessageBox.information(self, "Login Error", error_message)
            print(f"Login error: {e}")

    def signup(self):
        username = self.lineEdit_5.text()
        password = self.lineEdit_6.text()
        json_body = {"username": username, "password": password}
        api_url = f"{base_url}/api/v1/auth/signup"

        try:
            response = requests.post(api_url, json=json_body)
            response.raise_for_status()
            response_json = response.json()
            user_data = response_json.get("data", {})
            self.access_token = user_data.get("accessToken")
            self.username = user_data.get("username")
            self.connect_to_server(self.access_token)
            self.tabWidget.setCurrentIndex(3)
            QMessageBox.information(self, "Signup Successful", "Signup was successful.")
        except requests.RequestException as e:
            error_message = (
                response.json().get("error", {}).get("message", "Unknown error")
            )
            QMessageBox.information(self, "Signup Error", error_message)
            print(f"Signup error: {e}")

    def update_password(self):
        oldPass = self.lineEdit_7.text()
        newPassword = self.lineEdit_9.text()
        confNewPass = self.lineEdit_8.text()
        json_body = {
            "oldPassword": oldPass,
            "newPassword": newPassword,
            "confNewPassword": confNewPass,
        }
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }
        api_url = f"{base_url}/api/v1/auth/update-password"

        try:
            response = requests.post(api_url, json=json_body, headers=headers)
            response.raise_for_status()
            QMessageBox.information(
                self, "Updated Successful", "Password was updated successful."
            )
        except requests.RequestException as e:
            error_message = (
                response.json().get("error", {}).get("message", "Unknown error")
            )
            QMessageBox.information(self, "Update Error", error_message)
            print(f"Update error: {e}")

    def send_message(self):
        message = f"{self.username}: {self.textEdit_4.toPlainText()}"
        encrypted_message = encrypt_message(message, SECRET_KEY)
        self.sio.emit("new_message", encrypted_message)
        self.textEdit_5.insertPlainText(f"me: {self.textEdit_4.toPlainText()}\n")
        self.textEdit_4.setPlainText("")

    def send_audio_message(self):
        filename = "output.wav"
        self.record_audio(filename)
        with open(filename, "rb") as audio_file:
            audio_data = base64.b64encode(audio_file.read()).decode("utf-8")
        self.sio.emit("new_audio_message", audio_data)
        self.textEdit_5.insertPlainText("Audio message sent\n")

    def record_audio(self, filename="output.wav", duration=10, fs=44100):
        print("Recording...")
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
        sd.wait()  # Wait until recording is finished
        write(filename, fs, recording)  # Save as WAV file
        print("Recording finished")

    def play_audio(self, filename):
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
