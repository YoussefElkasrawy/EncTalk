from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import *
from PyQt5.uic import loadUiType
import requests
import sys
import resources_rc
import socketio


# from ui_UI import Ui_MainWindow as ui


base_url = "https://real-time-chat-api-v1.onrender.com"


ui, _ = loadUiType(
    "D:/engineering year3/semester2/Secure Programming/Project/code/app/UI.ui"
)


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.UI_Changes()
        self.Handle_buttons()

        self.access_token = ""
        self.username = ""

        self.sio = socketio.Client()

        self.sio.on("connect", self.on_connect)
        self.sio.on("disconnect", self.on_disconnect)

        self.sio.on("user_online", self.on_new_message)
        self.sio.on("user_offline", self.on_new_message)
        self.sio.on("error", self.on_error)
        self.sio.on("new_message", self.on_new_encrypted_message)

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

    def on_connect(self):
        print("Connected to Socket.IO server.")

    def on_disconnect(self):
        print("Disconnected from Socket.IO server.")

    def on_error(self, error):
        QMessageBox.information(self, "Error", error)

    def on_new_message(self, message):
        self.textEdit_5.insertPlainText(f"{message}\n")

    def on_new_encrypted_message(self, encrypted_message):
        decrypted_message = encrypted_message
        self.textEdit_5.insertPlainText(decrypted_message.decode("utf-8") + "\n")

    def connect_to_server(self, token):
        server_url = base_url

        self.sio.connect(
            server_url,
            auth={"token": token},
            transports=["websocket"],
        )

        self.textEdit_5.insertPlainText(self.username + " join chat" + "\n")

    def login(self):
        print("Login")
        username = self.lineEdit_3.text()
        password = self.lineEdit_4.text()

        json_body = {
            "username": username,
            "password": password,
        }

        api_url = f"{base_url}/api/v1/auth/login"

        try:
            response = requests.post(api_url, json=json_body)

            if response.status_code == 200:
                response_json = response.json()

                user_data = response_json.get("data", {})
                access_token = user_data.get("accessToken")
                username = user_data.get("username")

                self.access_token = access_token
                self.username = username

                self.connect_to_server(access_token)

                self.tabWidget.setCurrentIndex(3)
                QMessageBox.information(
                    self, "Login Successful", "Login was successful."
                )
            else:
                error_message = (
                    response.json().get("error", {}).get("message", "Unknown error")
                )
                QMessageBox.information(self, "Login Error", error_message)

        except requests.RequestException as e:
            QMessageBox.information(self, "Network Error", str(e))

    def signup(self):
        print("signup")
        username = self.lineEdit_5.text()
        password = self.lineEdit_6.text()

        json_body = {
            "username": username,
            "password": password,
        }

        api_url = f"{base_url}/api/v1/auth/signup"

        try:
            response = requests.post(api_url, json=json_body)

            if response.status_code == 200:
                response_json = response.json()

                user_data = response_json.get("data", {})
                access_token = user_data.get("accessToken")
                username = user_data.get("username")

                self.access_token = access_token
                self.username = username

                self.connect_to_server(access_token)

                self.tabWidget.setCurrentIndex(3)
                QMessageBox.information(
                    self, "Signup Successful", "Signup was successful."
                )
            else:
                error_message = (
                    response.json().get("error", {}).get("message", "Unknown error")
                )
                QMessageBox.information(self, "Signup Error", error_message)

        except requests.RequestException as e:
            QMessageBox.information(self, "Network Error", str(e))

    def update_password(self):
        print("Update Password")
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

            if response.status_code == 200:
                response_json = response.json()

                QMessageBox.information(
                    self, "Updated Successful", "Password was updated successful."
                )
            else:
                error_message = (
                    response.json().get("error", {}).get("message", "Unknown error")
                )
                QMessageBox.information(self, "Login Error", error_message)

        except requests.RequestException as e:
            QMessageBox.information(self, "Network Error", str(e))

    def send_message(self):
        message = f"{self.username}: {str(self.textEdit_4.toPlainText())}"
        self.sio.emit("new_message", message)
        self.textEdit_5.insertPlainText(
            f"me: {str(self.textEdit_4.toPlainText())}" + "\n"
        )
        self.textEdit_4.setPlainText("")


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
