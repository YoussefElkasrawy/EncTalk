from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import *
from PyQt5.uic import loadUiType
import resources_rc
import requests
import sys
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
import base64
import numpy as np
import random
import time

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


class Comp:
    def empty_frame(self):
        obj_n = str(random.random())
        self.frame = QFrame()
        self.frame.setObjectName(f"chat_frame_{obj_n}")
        self.frame.setLayoutDirection(Qt.RightToLeft)
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setMaximumSize(QSize(317, 50))

        return self.frame

    def msg_frame(self, msg):
        obj_n = msg + str(random.random())
        self.frame = QFrame()
        self.frame.setObjectName(f"chat_frame_{obj_n}")
        self.frame.setLayoutDirection(Qt.RightToLeft)
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setMaximumSize(QSize(317, 50))
        self.frame.setStyleSheet(
            "QFrame{\n"
            'font: 9pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "background-color: #ffffff;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 5px;\n"
            "}\n"
            "\n"
            "QLabel{\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;\n"
            "}\n"
            "\n"
        )

        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(f"gridLayout_chat_{obj_n}")

        self.msg = QLabel(self.frame)
        self.msg.setObjectName(f"msg_f_{obj_n}")
        self.msg.setText(f"{str(msg)}")
        self.msg.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.msg, 1, 3, 2, 1)

        return self.frame

    def audio_frame(self, audio_filename):
        obj_n = audio_filename + str(random.random())
        self.frame = QFrame()
        self.frame.setObjectName(f"audio_frame_{obj_n}")
        self.frame.setLayoutDirection(Qt.RightToLeft)
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setMaximumSize(QSize(317, 50))
        self.frame.setStyleSheet(
            "QFrame{\n"
            "background-color: #ffffff;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 5px;\n"
            "}\n"
        )

        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(f"gridLayout_audio_{obj_n}")

        self.play_button = QPushButton("Play", self.frame)
        self.play_button.setObjectName(f"play_btn_{obj_n}")
        self.play_button.clicked.connect(lambda: self.play_audio(audio_filename))

        self.stop_button = QPushButton("Stop", self.frame)
        self.stop_button.setObjectName(f"stop_btn_{obj_n}")
        self.stop_button.clicked.connect(self.stop_audio)

        self.gridLayout.addWidget(self.play_button, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.stop_button, 1, 2, 1, 1)

        return self.frame

    def play_audio(self, filename):
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

    def stop_audio(self):
        pygame.mixer.music.stop()


class MainApp(QMainWindow, ui):
    message_received = pyqtSignal(str, bool)
    audio_received = pyqtSignal(str, bool)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.UI_Changes()
        self.Handle_buttons()

        self.audio_folder = "audio_messages"
        os.makedirs(self.audio_folder, exist_ok=True)

        self.is_recording = False
        self.audio_data = []
        self.sio = socketio.Client()

        self.sio.on("connect", self.on_connect)
        self.sio.on("disconnect", self.on_disconnect)
        self.sio.on("user_online", self.on_new_message)
        self.sio.on("user_offline", self.on_new_message)
        self.sio.on("error", self.on_error)
        self.sio.on("new_message", self.on_enc_new_message)
        self.sio.on("new_audio_message", self.on_new_audio_message)

        self.message_received.connect(self.display_message)
        self.audio_received.connect(self.display_audio_message)

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
        self.toolButton_14.clicked.connect(self.toggle_recording)

    def on_connect(self):
        print("Connected to Socket.IO server.")

    def on_disconnect(self):
        print("Disconnected from Socket.IO server.")

    def on_error(self, error):
        QMessageBox.information(self, "Error", error)

    def on_new_message(self, message):
        self.message_received.emit(message, False)

    def on_enc_new_message(self, message):
        decrypted_message = decrypt_message(message, SECRET_KEY)
        self.message_received.emit(decrypted_message, False)

    def on_new_audio_message(self, audio_data):
        self.audio_received.emit(audio_data, False)

    def connect_to_server(self, token):
        server_url = base_url
        self.sio.connect(server_url, auth={"token": token}, transports=["websocket"])
        self.display_message(self.username + " joined chat", True)

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
            response = requests.put(api_url, json=json_body, headers=headers)
            response.raise_for_status()
            QMessageBox.information(
                self, "Password Update Successful", "Password update was successful."
            )
        except requests.RequestException as e:
            error_message = (
                response.json().get("error", {}).get("message", "Unknown error")
            )
            QMessageBox.information(self, "Password Update Error", error_message)
            print(f"Password update error: {e}")

    def send_message(self):
        message = f"{self.username}: {self.textEdit_4.toPlainText()}"
        if message:
            encrypted_message = encrypt_message(message, SECRET_KEY)
            self.sio.emit("new_message", encrypted_message)
            self.display_message(f"{self.textEdit_4.toPlainText()}", True)
            self.textEdit_4.setPlainText("")

    def toggle_recording(self):
        if self.is_recording:
            self.stop_recording()
        else:
            self.start_recording()

    def start_recording(self):
        self.is_recording = True
        self.audio_data = []
        self.audio_stream = sd.InputStream(callback=self.audio_callback)
        self.audio_stream.start()

    def stop_recording(self):
        self.is_recording = False
        self.audio_stream.stop()
        self.audio_stream.close()

        filename = os.path.join(
            self.audio_folder, f"s_audio_message_{str(time.time())}.wav"
        )
        write(filename, 44100, np.array(self.audio_data))

        with open(filename, "rb") as audio_file:
            encoded_audio = base64.b64encode(audio_file.read()).decode("utf-8")
            self.sio.emit("new_audio_message", encoded_audio)
            self.display_audio_message(encoded_audio, True)

    def audio_callback(self, indata, frames, time, status):
        self.audio_data.extend(indata.copy())

    @pyqtSlot(str, bool)
    def display_message(self, message, is_user_message):
        msg_frame = Comp().msg_frame(message)
        if is_user_message:
            self.verticalLayout_3.addWidget(msg_frame)
            self.verticalLayout.addWidget(Comp().empty_frame())
        else:
            self.verticalLayout.addWidget(msg_frame)
            self.verticalLayout_3.addWidget(Comp().empty_frame())

    @pyqtSlot(str, bool)
    def display_audio_message(self, encoded_audio, is_user_message):
        decoded_audio = base64.b64decode(encoded_audio)
        filename = os.path.join(
            self.audio_folder, f"r_audio_message_{str(time.time())}.wav"
        )
        with open(filename, "wb") as audio_file:
            audio_file.write(decoded_audio)

        audio_frame = Comp().audio_frame(filename)
        if is_user_message:
            self.verticalLayout_3.addWidget(audio_frame)
            self.verticalLayout.addWidget(Comp().empty_frame())
        else:
            self.verticalLayout.addWidget(audio_frame)
            self.verticalLayout_3.addWidget(Comp().empty_frame())


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
