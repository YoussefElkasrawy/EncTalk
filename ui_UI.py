from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import *
import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 725)
        MainWindow.setMinimumSize(QSize(700, 725))
        MainWindow.setMaximumSize(QSize(700, 725))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(39, 39, 39, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
        # endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(255, 255, 255, 128))
        brush3.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
        # endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
        # endif
        MainWindow.setPalette(palette)
        MainWindow.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(
            ":/images/icons/cil-lock-locked.png", QSize(), QIcon.Normal, QIcon.Off
        )
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(
            "background-color: rgb(39, 39, 39);\n" "color: rgb(255, 255, 255);"
        )
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setStyleSheet(
            "QTabWidget\n"
            "{\n"
            "	border-style: solid;\n"
            "	border-top-color: transparent;\n"
            "	border-right-color: transparent;\n"
            "	border-left-color: transparent;\n"
            "	border-bottom-color: transparent;\n"
            "	border-width: 0px;\n"
            "}"
        )
        self.logintab = QWidget()
        self.logintab.setObjectName("logintab")
        self.gridLayout_2 = QGridLayout(self.logintab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_23 = QFrame(self.logintab)
        self.frame_23.setObjectName("frame_23")
        self.frame_23.setStyleSheet(
            "QLineEdit \n"
            "{\n"
            "	border-radius: 8px;\n"
            "	border-width: 2px;\n"
            "	border-style: solid;\n"
            "	border-color: #00a884;\n"
            '	font: 13pt "Arial Rounded MT Bold";\n'
            "}\n"
            ""
        )
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_29 = QGridLayout(self.frame_23)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.gridLayout_29.setHorizontalSpacing(25)
        self.gridLayout_29.setVerticalSpacing(0)
        self.gridLayout_29.setContentsMargins(25, 25, 25, 25)
        self.frame = QFrame(self.frame_23)
        self.frame.setObjectName("frame")
        self.frame.setMinimumSize(QSize(480, 70))
        self.frame.setMaximumSize(QSize(480, 70))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.login_btn = QToolButton(self.frame)
        self.login_btn.setObjectName("login_btn")
        self.login_btn.setMinimumSize(QSize(380, 50))
        self.login_btn.setMaximumSize(QSize(380, 50))
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

        self.gridLayout_6.addWidget(self.login_btn, 0, 0, 1, 1)

        self.toolButton_11 = QToolButton(self.frame)
        self.toolButton_11.setObjectName("toolButton_11")
        self.toolButton_11.setMinimumSize(QSize(50, 50))
        self.toolButton_11.setMaximumSize(QSize(50, 50))
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
        icon1 = QIcon()
        icon1.addFile(
            ":/images/icons/cil-medical-cross.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.toolButton_11.setIcon(icon1)

        self.gridLayout_6.addWidget(self.toolButton_11, 0, 1, 1, 1)

        self.gridLayout_29.addWidget(self.frame, 2, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame_23)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(480, 50))
        self.lineEdit_3.setMaximumSize(QSize(480, 50))
        self.lineEdit_3.setStyleSheet("")
        self.lineEdit_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.lineEdit_3, 0, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame_23)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(480, 50))
        self.lineEdit_4.setMaximumSize(QSize(480, 50))
        self.lineEdit_4.setStyleSheet('font: 13pt "Arial Rounded MT Bold";')
        self.lineEdit_4.setEchoMode(QLineEdit.Password)
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.lineEdit_4, 1, 0, 1, 1)

        self.gridLayout_2.addWidget(self.frame_23, 1, 0, 1, 1)

        self.tabWidget.addTab(self.logintab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_24 = QFrame(self.tab_2)
        self.frame_24.setObjectName("frame_24")
        self.frame_24.setStyleSheet(
            "QLineEdit \n"
            "{\n"
            "	border-radius: 8px;\n"
            "	border-width: 2px;\n"
            "	border-style: solid;\n"
            "	border-color: #00a884;\n"
            '	font: 13pt "Arial Rounded MT Bold";\n'
            "}\n"
            ""
        )
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_24)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.gridLayout_30.setHorizontalSpacing(25)
        self.gridLayout_30.setVerticalSpacing(0)
        self.gridLayout_30.setContentsMargins(25, 25, 25, 25)
        self.frame_2 = QFrame(self.frame_24)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setMinimumSize(QSize(480, 70))
        self.frame_2.setMaximumSize(QSize(480, 70))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.signup_btn = QToolButton(self.frame_2)
        self.signup_btn.setObjectName("signup_btn")
        self.signup_btn.setMinimumSize(QSize(380, 50))
        self.signup_btn.setMaximumSize(QSize(380, 50))
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

        self.gridLayout_7.addWidget(self.signup_btn, 0, 0, 1, 1)

        self.toolButton_12 = QToolButton(self.frame_2)
        self.toolButton_12.setObjectName("toolButton_12")
        self.toolButton_12.setMinimumSize(QSize(50, 50))
        self.toolButton_12.setMaximumSize(QSize(50, 50))
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
        icon2 = QIcon()
        icon2.addFile(
            ":/images/icons/cil-account-logout.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.toolButton_12.setIcon(icon2)

        self.gridLayout_7.addWidget(self.toolButton_12, 0, 1, 1, 1)

        self.gridLayout_30.addWidget(self.frame_2, 2, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.frame_24)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(480, 50))
        self.lineEdit_5.setMaximumSize(QSize(480, 50))
        self.lineEdit_5.setStyleSheet("")
        self.lineEdit_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_30.addWidget(self.lineEdit_5, 0, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.frame_24)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(480, 50))
        self.lineEdit_6.setMaximumSize(QSize(480, 50))
        self.lineEdit_6.setStyleSheet('font: 13pt "Arial Rounded MT Bold";')
        self.lineEdit_6.setEchoMode(QLineEdit.Password)
        self.lineEdit_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_30.addWidget(self.lineEdit_6, 1, 0, 1, 1)

        self.gridLayout_3.addWidget(self.frame_24, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_26 = QFrame(self.tab)
        self.frame_26.setObjectName("frame_26")
        self.frame_26.setMinimumSize(QSize(0, 80))
        self.frame_26.setMaximumSize(QSize(16777215, 80))
        self.frame_26.setStyleSheet("background-color: rgb(32, 32, 32);")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.gridLayout_31 = QGridLayout(self.frame_26)
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.horizontalSpacer_8 = QSpacerItem(
            874, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_31.addItem(self.horizontalSpacer_8, 0, 1, 1, 1)

        self.toolButton_13 = QToolButton(self.frame_26)
        self.toolButton_13.setObjectName("toolButton_13")
        self.toolButton_13.setMinimumSize(QSize(50, 50))
        self.toolButton_13.setMaximumSize(QSize(50, 50))
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
        icon3 = QIcon()
        icon3.addFile(
            ":/images/icons/cil-chat-bubble.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.toolButton_13.setIcon(icon3)

        self.gridLayout_31.addWidget(self.toolButton_13, 0, 0, 1, 1)

        self.gridLayout_4.addWidget(self.frame_26, 0, 0, 1, 1)

        self.frame_27 = QFrame(self.tab)
        self.frame_27.setObjectName("frame_27")
        self.frame_27.setStyleSheet(
            "QLineEdit \n"
            "{\n"
            "	border-radius: 8px;\n"
            "	border-width: 2px;\n"
            "	border-style: solid;\n"
            "	border-color: #00a884;\n"
            '	font: 13pt "Arial Rounded MT Bold";\n'
            "}\n"
            ""
        )
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.gridLayout_32 = QGridLayout(self.frame_27)
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.gridLayout_32.setHorizontalSpacing(25)
        self.gridLayout_32.setVerticalSpacing(0)
        self.gridLayout_32.setContentsMargins(25, 25, 25, 25)
        self.lineEdit_8 = QLineEdit(self.frame_27)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(430, 50))
        self.lineEdit_8.setMaximumSize(QSize(430, 50))
        self.lineEdit_8.setStyleSheet('font: 13pt "Arial Rounded MT Bold";')
        self.lineEdit_8.setEchoMode(QLineEdit.Password)
        self.lineEdit_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_32.addWidget(self.lineEdit_8, 2, 0, 1, 1)

        self.login_toolButton_3 = QToolButton(self.frame_27)
        self.login_toolButton_3.setObjectName("login_toolButton_3")
        self.login_toolButton_3.setMinimumSize(QSize(430, 50))
        self.login_toolButton_3.setMaximumSize(QSize(430, 50))
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

        self.gridLayout_32.addWidget(self.login_toolButton_3, 3, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.frame_27)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(430, 50))
        self.lineEdit_7.setMaximumSize(QSize(430, 50))
        self.lineEdit_7.setStyleSheet("")
        self.lineEdit_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_32.addWidget(self.lineEdit_7, 0, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.frame_27)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(430, 50))
        self.lineEdit_9.setMaximumSize(QSize(430, 50))
        self.lineEdit_9.setStyleSheet("")
        self.lineEdit_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_32.addWidget(self.lineEdit_9, 1, 0, 1, 1)

        self.gridLayout_4.addWidget(self.frame_27, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_28 = QFrame(self.tab_3)
        self.frame_28.setObjectName("frame_28")
        self.frame_28.setMinimumSize(QSize(0, 80))
        self.frame_28.setMaximumSize(QSize(16777215, 80))
        self.frame_28.setStyleSheet("background-color: rgb(32, 32, 32);")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.gridLayout_33 = QGridLayout(self.frame_28)
        self.gridLayout_33.setObjectName("gridLayout_33")
        self.horizontalSpacer_9 = QSpacerItem(
            874, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_33.addItem(self.horizontalSpacer_9, 0, 1, 1, 1)

        self.toolButton_10 = QToolButton(self.frame_28)
        self.toolButton_10.setObjectName("toolButton_10")
        self.toolButton_10.setMinimumSize(QSize(50, 50))
        self.toolButton_10.setMaximumSize(QSize(50, 50))
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
        icon4 = QIcon()
        icon4.addFile(
            ":/images/icons/cil-settings.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.toolButton_10.setIcon(icon4)

        self.gridLayout_33.addWidget(self.toolButton_10, 0, 0, 1, 1)

        self.gridLayout_5.addWidget(self.frame_28, 0, 0, 1, 1)

        self.frame_12 = QFrame(self.tab_3)
        self.frame_12.setObjectName("frame_12")
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
            "	border-radius: 8px;\n"
            ""
            "	border-width: 2px;\n"
            "	border-style: solid;\n"
            "	border-color: #00a884;\n"
            '	font: 13pt "Arial Rounded MT Bold";\n'
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
            "   background: transpare"
            "nt;\n"
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
            "	\n"
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
            ""
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
            "   background: transp"
            "arent;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "   background-color: #222222;\n"
            "	\n"
            "}\n"
            ""
        )
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.frame_12)
        self.gridLayout_26.setSpacing(5)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.gridLayout_26.setContentsMargins(10, 10, 10, 10)
        self.frame_21 = QFrame(self.frame_12)
        self.frame_21.setObjectName("frame_21")
        self.frame_21.setMinimumSize(QSize(0, 70))
        self.frame_21.setMaximumSize(QSize(16777215, 70))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_21)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.textEdit_4 = QTextEdit(self.frame_21)
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_4.setMinimumSize(QSize(0, 50))
        self.textEdit_4.setMaximumSize(QSize(16777215, 50))
        self.textEdit_4.setStyleSheet('font: 11pt "MS Shell Dlg 2";')

        self.gridLayout_25.addWidget(self.textEdit_4, 0, 0, 1, 1)

        self.toolButton_9 = QToolButton(self.frame_21)
        self.toolButton_9.setObjectName("toolButton_9")
        self.toolButton_9.setMinimumSize(QSize(50, 50))
        self.toolButton_9.setMaximumSize(QSize(50, 50))
        icon5 = QIcon()
        icon5.addFile(":/images/icons/cil-cursor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_9.setIcon(icon5)

        self.gridLayout_25.addWidget(self.toolButton_9, 0, 1, 1, 1)

        self.gridLayout_26.addWidget(self.frame_21, 1, 0, 1, 1)

        self.textEdit_5 = QTextEdit(self.frame_12)
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_5.setEnabled(False)
        self.textEdit_5.setStyleSheet('font: 12pt "Arial Rounded MT Bold";')

        self.gridLayout_26.addWidget(self.textEdit_5, 0, 0, 1, 1)

        self.gridLayout_5.addWidget(self.frame_12, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "CHAT", None)
        )
        self.login_btn.setText(QCoreApplication.translate("MainWindow", "Login", None))
        # if QT_CONFIG(shortcut)
        self.login_btn.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.toolButton_11.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_11.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        # if QT_CONFIG(statustip)
        self.lineEdit_3.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.lineEdit_3.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "username", None)
        )
        self.lineEdit_4.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "password", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.logintab),
            QCoreApplication.translate("MainWindow", "Tab 1", None),
        )
        self.signup_btn.setText(
            QCoreApplication.translate("MainWindow", "Signup", None)
        )
        # if QT_CONFIG(shortcut)
        self.signup_btn.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.toolButton_12.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_12.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        # if QT_CONFIG(statustip)
        self.lineEdit_5.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.lineEdit_5.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "username", None)
        )
        self.lineEdit_6.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "password", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            QCoreApplication.translate("MainWindow", "Tab 2", None),
        )
        self.toolButton_13.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_13.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.lineEdit_8.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Confirm New Password", None)
        )
        self.login_toolButton_3.setText(
            QCoreApplication.translate("MainWindow", "Update Password", None)
        )
        # if QT_CONFIG(shortcut)
        self.login_toolButton_3.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        # if QT_CONFIG(statustip)
        self.lineEdit_7.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.lineEdit_7.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Old Password", None)
        )
        # if QT_CONFIG(statustip)
        self.lineEdit_9.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        self.lineEdit_9.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "New Password", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QCoreApplication.translate("MainWindow", "Page", None),
        )
        self.toolButton_10.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_10.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.toolButton_9.setText("")
        # if QT_CONFIG(shortcut)
        self.toolButton_9.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_3),
            QCoreApplication.translate("MainWindow", "Page", None),
        )

    # retranslateUi
