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
        self.frame.setMinimumSize(QSize(0, 70))
        self.frame.setMaximumWidth(317)
        self.frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        return self.frame

    def msg_frame(self, msg):
        obj_n = str(random.random())
        self.frame = QFrame()
        self.frame.setObjectName(f"chat_frame_{obj_n}")
        self.frame.setLayoutDirection(Qt.RightToLeft)
        self.frame.setMinimumSize(QSize(0, 70))
        self.frame.setMaximumWidth(317)
        self.frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.frame.setStyleSheet(
            "QFrame {"
            "   font: 9pt 'Arial';"
            "   color: #1e1d23;"
            "   background-color: #dcf8c6;"  # WhatsApp light green background
            "   border-width: 1px;"
            "   border-style: solid;"
            "   border-radius: 10px;"
            "   padding: 5px;"
            "}"
            "QLabel {"
            "   font: 11pt 'Arial';"
            "   color: #1e1d23;"
            "}"
        )
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(f"gridLayout_chat_{obj_n}")

        self.username_label = QLabel(self.frame)
        self.username_label.setObjectName(f"username_{obj_n}")
        self.username_label.setText(msg["username"])
        self.username_label.setAlignment(Qt.AlignLeft)

        self.time_label = QLabel(self.frame)
        self.time_label.setObjectName(f"time_{obj_n}")
        self.time_label.setText(msg["time"])
        self.time_label.setAlignment(Qt.AlignRight)

        self.msg = QLabel(self.frame)
        self.msg.setObjectName(f"msg_f_{obj_n}")
        self.msg.setText(f"{str(msg['data'])}")
        self.msg.setWordWrap(True)
        self.msg.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.gridLayout.addWidget(self.username_label, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.time_label, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.msg, 1, 0, 1, 3)

        return self.frame

    def audio_frame(self, audio_message):
        obj_n = audio_message["data"] + str(random.random())
        self.frame = QFrame()
        self.frame.setObjectName(f"audio_frame_{obj_n}")
        self.frame.setLayoutDirection(Qt.RightToLeft)
        self.frame.setMinimumSize(QSize(0, 70))
        self.frame.setMaximumWidth(317)
        self.frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.frame.setStyleSheet(
            "QFrame {"
            "   font: 9pt 'Arial';"
            "   color: #1e1d23;"
            "   background-color: #dcf8c6;"  # WhatsApp light green background
            "   border-width: 1px;"
            "   border-style: solid;"
            "   border-radius: 10px;"
            "   padding: 5px;"
            "}"
        )

        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(f"gridLayout_audio_{obj_n}")

        self.username_label = QLabel(self.frame)
        self.username_label.setObjectName(f"username_{obj_n}")
        self.username_label.setText(audio_message["username"])
        self.username_label.setAlignment(Qt.AlignLeft)

        self.time_label = QLabel(self.frame)
        self.time_label.setObjectName(f"time_{obj_n}")
        self.time_label.setText(audio_message["time"])
        self.time_label.setAlignment(Qt.AlignRight)

        self.play_button = QPushButton("Play", self.frame)
        self.play_button.setObjectName(f"play_btn_{obj_n}")
        self.play_button.clicked.connect(lambda: self.play_audio(audio_message["data"]))

        self.stop_button = QPushButton("Stop", self.frame)
        self.stop_button.setObjectName(f"stop_btn_{obj_n}")
        self.stop_button.clicked.connect(self.stop_audio)

        self.gridLayout.addWidget(self.username_label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.time_label, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.play_button, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.stop_button, 1, 1, 1, 1)

        return self.frame

    def play_audio(self, filename):
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

    def stop_audio(self):
        pygame.mixer.music.stop()


class MainApp(QMainWindow, ui):
    message_received = pyqtSignal(dict, bool)
    audio_received = pyqtSignal(dict, bool)

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
        self.signup_btn.clicked.connect(self.signup)
        self.login_btn.clicked.connect(self.login)
        self.up_btn.clicked.connect(self.update_password)
        self.toolButton_9.clicked.connect(self.send_message)
        self.toolButton_14.pressed.connect(self.start_recording)
        self.toolButton_14.released.connect(self.stop_recording)

    def connect_to_server(self, token):
        server_url = base_url
        self.sio.connect(server_url, auth={"token": token}, transports=["websocket"])

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
        message = self.textEdit_4.toPlainText()
        if len(message) == 0:
            self.label_10.setText("Cannot send empty message")
        else:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            encrypted_message = encrypt_message(
                str({"username": self.username, "data": message, "time": timestamp}),
                SECRET_KEY,
            )
            self.sio.emit("new_message", encrypted_message)
            self.textEdit_4.setText("")
            self.message_received.emit(
                {"username": self.username, "data": message, "time": timestamp}, True
            )

    def start_recording(self):
        icon = QIcon()
        icon.addFile(
            ":/images/icons/cil-media-pause.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.toolButton_14.setIcon(icon)

        self.is_recording = True
        self.audio_data = []
        self.stream = sd.InputStream(callback=self.audio_callback)
        self.stream.start()

    def stop_recording(self):
        icon = QIcon()
        icon.addFile(
            ":/images/icons/cil-microphone.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.toolButton_14.setIcon(icon)

        self.is_recording = False
        self.stream.stop()
        self.stream.close()

        audio_data = np.concatenate(self.audio_data, axis=0)
        audio_data = np.int16(audio_data * 32767)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        filename = os.path.join(
            self.audio_folder, f"{self.username}_{str(time.time())}.wav"
        )
        write(filename, 44100, audio_data)
        with open(filename, "rb") as audio_file:
            encoded_audio = base64.b64encode(audio_file.read()).decode()
            self.sio.emit(
                "new_audio_message",
                {
                    "username": self.username,
                    "data": encoded_audio,
                    "time": timestamp,
                },
            )
            self.audio_received.emit(
                {"username": self.username, "data": filename, "time": timestamp}, True
            )

    def audio_callback(self, indata, frames, time, status):
        if self.is_recording:
            self.audio_data.append(indata.copy())

    def on_connect(self):
        print("Connected to server")

    def on_disconnect(self):
        print("Disconnected from server")

    def on_error(self, error):
        print("Error:", error)

    def on_new_message(self, message):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        message = {"username": "server", "data": message, "time": timestamp}
        self.message_received.emit(message, False)

    def on_enc_new_message(self, message):
        decrypted_message = decrypt_message(message, SECRET_KEY)
        message_data = eval(decrypted_message)
        self.message_received.emit(message_data, False)

    def on_new_audio_message(self, audio_message):
        audio_message["data"] = base64.b64decode(audio_message["data"])
        filename = os.path.join(
            self.audio_folder, f"r_audio_message_{str(time.time())}.wav"
        )
        with open(filename, "wb") as audio_file:
            audio_file.write(audio_message["data"])
        audio_message["data"] = filename
        self.audio_received.emit(audio_message, False)

    @pyqtSlot(dict, bool)
    def display_message(self, message, is_user_message):
        msg_frame = Comp().msg_frame(message)
        if is_user_message:
            self.verticalLayout_3.addWidget(msg_frame)
            self.verticalLayout.addWidget(Comp().empty_frame())
        else:
            self.verticalLayout.addWidget(msg_frame)
            self.verticalLayout_3.addWidget(Comp().empty_frame())

    @pyqtSlot(dict, bool)
    def display_audio_message(self, audio_message, is_user_message):
        audio_frame = Comp().audio_frame(audio_message)
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
    app.exec_()


if __name__ == "__main__":
    main()
