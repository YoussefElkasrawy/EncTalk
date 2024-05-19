from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import *
import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 725)
        MainWindow.setMinimumSize(QtCore.QSize(700, 725))
        MainWindow.setMaximumSize(QtCore.QSize(700, 725))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/images/icons/cil-lock-locked.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(
            "background-color: rgb(39, 39, 39);\n" "color: rgb(255, 255, 255);"
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet(
            "QTabWidget\n"
            "{\n"
            "    border-style: solid;\n"
            "    border-top-color: transparent;\n"
            "    border-right-color: transparent;\n"
            "    border-left-color: transparent;\n"
            "    border-bottom-color: transparent;\n"
            "    border-width: 0px;\n"
            "}"
        )
        self.tabWidget.setObjectName("tabWidget")
        self.logintab = QtWidgets.QWidget()
        self.logintab.setObjectName("logintab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.logintab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_23 = QtWidgets.QFrame(self.logintab)
        self.frame_23.setStyleSheet(
            "QLineEdit \n"
            "{\n"
            "    border-radius: 8px;\n"
            "    border-width: 2px;\n"
            "    border-style: solid;\n"
            "    border-color: #00a884;\n"
            '    font: 13pt "Arial Rounded MT Bold";\n'
            "}\n"
            ""
        )
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.frame_23)
        self.gridLayout_29.setContentsMargins(25, 25, 25, 25)
        self.gridLayout_29.setHorizontalSpacing(25)
        self.gridLayout_29.setVerticalSpacing(0)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.frame = QtWidgets.QFrame(self.frame_23)
        self.frame.setMinimumSize(QtCore.QSize(480, 70))
        self.frame.setMaximumSize(QtCore.QSize(480, 70))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.login_btn = QtWidgets.QToolButton(self.frame)
        self.login_btn.setMinimumSize(QtCore.QSize(380, 50))
        self.login_btn.setMaximumSize(QtCore.QSize(380, 50))
        self.login_btn.setStyleSheet(
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}"
        )
        self.login_btn.setObjectName("login_btn")
        self.gridLayout_6.addWidget(self.login_btn, 0, 0, 1, 1)
        self.toolButton_11 = QtWidgets.QToolButton(self.frame)
        self.toolButton_11.setMinimumSize(QtCore.QSize(50, 50))
        self.toolButton_11.setMaximumSize(QtCore.QSize(50, 50))
        self.toolButton_11.setStyleSheet(
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}"
        )
        self.toolButton_11.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/images/icons/cil-medical-cross.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.toolButton_11.setIcon(icon1)
        self.toolButton_11.setObjectName("toolButton_11")
        self.gridLayout_6.addWidget(self.toolButton_11, 0, 1, 1, 1)
        self.gridLayout_29.addWidget(self.frame, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_23)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(480, 50))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(480, 50))
        self.lineEdit_3.setStatusTip("")
        self.lineEdit_3.setStyleSheet("")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_29.addWidget(self.lineEdit_3, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_23)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(480, 50))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(480, 50))
        self.lineEdit_4.setStyleSheet('font: 13pt "Arial Rounded MT Bold";')
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_29.addWidget(self.lineEdit_4, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_23, 1, 0, 1, 1)
        self.tabWidget.addTab(self.logintab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_24 = QtWidgets.QFrame(self.tab_2)
        self.frame_24.setStyleSheet(
            "QLineEdit \n"
            "{\n"
            "    border-radius: 8px;\n"
            "    border-width: 2px;\n"
            "    border-style: solid;\n"
            "    border-color: #00a884;\n"
            '    font: 13pt "Arial Rounded MT Bold";\n'
            "}\n"
            ""
        )
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.gridLayout_30 = QtWidgets.QGridLayout(self.frame_24)
        self.gridLayout_30.setContentsMargins(25, 25, 25, 25)
        self.gridLayout_30.setHorizontalSpacing(25)
        self.gridLayout_30.setVerticalSpacing(0)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.frame_2 = QtWidgets.QFrame(self.frame_24)
        self.frame_2.setMinimumSize(QtCore.QSize(480, 70))
        self.frame_2.setMaximumSize(QtCore.QSize(480, 70))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.signup_btn = QtWidgets.QToolButton(self.frame_2)
        self.signup_btn.setMinimumSize(QtCore.QSize(380, 50))
        self.signup_btn.setMaximumSize(QtCore.QSize(380, 50))
        self.signup_btn.setStyleSheet(
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}"
        )
        self.signup_btn.setObjectName("signup_btn")
        self.gridLayout_7.addWidget(self.signup_btn, 0, 0, 1, 1)
        self.toolButton_12 = QtWidgets.QToolButton(self.frame_2)
        self.toolButton_12.setMinimumSize(QtCore.QSize(50, 50))
        self.toolButton_12.setMaximumSize(QtCore.QSize(50, 50))
        self.toolButton_12.setStyleSheet(
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}"
        )
        self.toolButton_12.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/images/icons/cil-account-logout.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.toolButton_12.setIcon(icon2)
        self.toolButton_12.setObjectName("toolButton_12")
        self.gridLayout_7.addWidget(self.toolButton_12, 0, 1, 1, 1)
        self.gridLayout_30.addWidget(self.frame_2, 2, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_24)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(480, 50))
        self.lineEdit_5.setMaximumSize(QtCore.QSize(480, 50))
        self.lineEdit_5.setStatusTip("")
        self.lineEdit_5.setStyleSheet("")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_30.addWidget(self.lineEdit_5, 0, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_24)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(480, 50))
        self.lineEdit_6.setMaximumSize(QtCore.QSize(480, 50))
        self.lineEdit_6.setStyleSheet('font: 13pt "Arial Rounded MT Bold";')
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_30.addWidget(self.lineEdit_6, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_24, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_26 = QtWidgets.QFrame(self.tab)
        self.frame_26.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_26.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_26.setStyleSheet("background-color: rgb(32, 32, 32);")
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.gridLayout_31 = QtWidgets.QGridLayout(self.frame_26)
        self.gridLayout_31.setObjectName("gridLayout_31")
        spacerItem = QtWidgets.QSpacerItem(
            874, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_31.addItem(spacerItem, 0, 1, 1, 1)
        self.toolButton_13 = QtWidgets.QToolButton(self.frame_26)
        self.toolButton_13.setMinimumSize(QtCore.QSize(50, 50))
        self.toolButton_13.setMaximumSize(QtCore.QSize(50, 50))
        self.toolButton_13.setStyleSheet(
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}"
        )
        self.toolButton_13.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(":/images/icons/cil-chat-bubble.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.toolButton_13.setIcon(icon3)
        self.toolButton_13.setObjectName("toolButton_13")
        self.gridLayout_31.addWidget(self.toolButton_13, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_26, 0, 0, 1, 1)
        self.frame_27 = QtWidgets.QFrame(self.tab)
        self.frame_27.setStyleSheet(
            "QLineEdit \n"
            "{\n"
            "    border-radius: 8px;\n"
            "    border-width: 2px;\n"
            "    border-style: solid;\n"
            "    border-color: #00a884;\n"
            '    font: 13pt "Arial Rounded MT Bold";\n'
            "}\n"
            ""
        )
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.gridLayout_32 = QtWidgets.QGridLayout(self.frame_27)
        self.gridLayout_32.setContentsMargins(25, 25, 25, 25)
        self.gridLayout_32.setHorizontalSpacing(25)
        self.gridLayout_32.setVerticalSpacing(0)
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_27)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(430, 50))
        self.lineEdit_8.setMaximumSize(QtCore.QSize(430, 50))
        self.lineEdit_8.setStyleSheet('font: 13pt "Arial Rounded MT Bold";')
        self.lineEdit_8.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_32.addWidget(self.lineEdit_8, 2, 0, 1, 1)
        self.login_toolButton_3 = QtWidgets.QToolButton(self.frame_27)
        self.login_toolButton_3.setMinimumSize(QtCore.QSize(430, 50))
        self.login_toolButton_3.setMaximumSize(QtCore.QSize(430, 50))
        self.login_toolButton_3.setStyleSheet(
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}"
        )
        self.login_toolButton_3.setObjectName("login_toolButton_3")
        self.gridLayout_32.addWidget(self.login_toolButton_3, 3, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_27)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(430, 50))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(430, 50))
        self.lineEdit_7.setStatusTip("")
        self.lineEdit_7.setStyleSheet("")
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_32.addWidget(self.lineEdit_7, 0, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_27)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(430, 50))
        self.lineEdit_9.setMaximumSize(QtCore.QSize(430, 50))
        self.lineEdit_9.setStatusTip("")
        self.lineEdit_9.setStyleSheet("")
        self.lineEdit_9.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_32.addWidget(self.lineEdit_9, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_27, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_28 = QtWidgets.QFrame(self.tab_3)
        self.frame_28.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_28.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_28.setStyleSheet("background-color: rgb(32, 32, 32);")
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.gridLayout_33 = QtWidgets.QGridLayout(self.frame_28)
        self.gridLayout_33.setObjectName("gridLayout_33")
        spacerItem1 = QtWidgets.QSpacerItem(
            874, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_33.addItem(spacerItem1, 0, 1, 1, 1)
        self.toolButton_10 = QtWidgets.QToolButton(self.frame_28)
        self.toolButton_10.setMinimumSize(QtCore.QSize(50, 50))
        self.toolButton_10.setMaximumSize(QtCore.QSize(50, 50))
        self.toolButton_10.setStyleSheet(
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            ""
        )
        self.toolButton_10.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap(":/images/icons/cil-settings.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.toolButton_10.setIcon(icon4)
        self.toolButton_10.setObjectName("toolButton_10")
        self.gridLayout_33.addWidget(self.toolButton_10, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_28, 0, 0, 1, 1)
        self.frame_12 = QtWidgets.QFrame(self.tab_3)
        self.frame_12.setStyleSheet(
            "QToolButton\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #2d2d2d;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QToolButton:hover\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #404040;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QTextEdit\n"
            "{\n"
            "border-radius: 10px;\n"
            "border-style: solid;\n"
            "border-top-color: transparent;\n"
            "border-right-color: transparent;\n"
            "border-left-color: transparent;\n"
            "border-bottom-color: transparent;\n"
            "border-width: 0px;\n"
            "background-color: #303030;\n"
            'font: 12pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QLineEdit \n"
            "{\n"
            "    border-radius: 8px;\n"
            "    border-width: 2px;\n"
            "    border-style: solid;\n"
            "    border-color: #00a884;\n"
            '    font: 13pt "Arial Rounded MT Bold";\n'
            "}\n"
            "\n"
            "QScrollBar:vertical \n"
            "{\n"
            "   border: none;\n"
            "   width: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "/*00a884*/\n"
            "QScrollBar::handle:vertical \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   width : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:vertical:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:vertical \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
            "{\n"
            "   background-color: #222222;\n"
            "    \n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   height: 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal \n"
            "{\n"
            "   border: none;\n"
            "   border-radius : 0px;\n"
            "   background-color: #00a884;\n"
            "   min-height: 80px;\n"
            "   height : 12px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::handle:horizontal:pressed\n"
            "{\n"
            "   background-color: #00a884; \n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal\n"
            "{\n"
            "   border: none;\n"
            "   background: transparent;\n"
            "   height: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:hover \n"
            "{\n"
            "   background-color: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::sub-line:horizontal:pressed \n"
            "{\n"
            "   background-color: #3f3f3f;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:horizontal\n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::down-arrow:horizontal \n"
            "{\n"
            "   width: 0px;\n"
            "   height: 0px;\n"
            "   background: transparent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "    \n"
            "}\n"
            ""
        )
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.frame_12)
        self.gridLayout_26.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_26.setSpacing(5)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.frame_21 = QtWidgets.QFrame(self.frame_12)
        self.frame_21.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_21.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.frame_21)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.textEdit_4 = QtWidgets.QTextEdit(self.frame_21)
        self.textEdit_4.setMinimumSize(QtCore.QSize(0, 50))
        self.textEdit_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.textEdit_4.setStyleSheet('font: 11pt "MS Shell Dlg 2";')
        self.textEdit_4.setObjectName("textEdit_4")
        self.gridLayout_25.addWidget(self.textEdit_4, 0, 0, 1, 1)
        self.toolButton_9 = QtWidgets.QToolButton(self.frame_21)
        self.toolButton_9.setMinimumSize(QtCore.QSize(50, 50))
        self.toolButton_9.setMaximumSize(QtCore.QSize(50, 50))
        self.toolButton_9.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap(":/images/icons/cil-cursor.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.toolButton_9.setIcon(icon5)
        self.toolButton_9.setObjectName("toolButton_9")
        self.gridLayout_25.addWidget(self.toolButton_9, 0, 1, 1, 1)
        self.gridLayout_26.addWidget(self.frame_21, 1, 0, 1, 1)
        self.textEdit_5 = QtWidgets.QTextEdit(self.frame_12)
        self.textEdit_5.setEnabled(False)
        self.textEdit_5.setStyleSheet('font: 12pt "Arial Rounded MT Bold";')
        self.textEdit_5.setObjectName("textEdit_5")
        self.gridLayout_26.addWidget(self.textEdit_5, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_12, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CHAT"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.login_btn.setShortcut(_translate("MainWindow", "Return"))
        self.toolButton_11.setShortcut(_translate("MainWindow", "Return"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "username"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "password"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.logintab), _translate("MainWindow", "Tab 1")
        )
        self.signup_btn.setText(_translate("MainWindow", "Signup"))
        self.signup_btn.setShortcut(_translate("MainWindow", "Return"))
        self.toolButton_12.setShortcut(_translate("MainWindow", "Return"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "username"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "password"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2")
        )
        self.toolButton_13.setShortcut(_translate("MainWindow", "Return"))
        self.lineEdit_8.setPlaceholderText(
            _translate("MainWindow", "Confirm New Password")
        )
        self.login_toolButton_3.setText(_translate("MainWindow", "Update Password"))
        self.login_toolButton_3.setShortcut(_translate("MainWindow", "Return"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "Old Password"))
        self.lineEdit_9.setPlaceholderText(_translate("MainWindow", "New Password"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Page")
        )
        self.toolButton_10.setShortcut(_translate("MainWindow", "Return"))
        self.toolButton_9.setShortcut(_translate("MainWindow", "Return"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page")
        )
