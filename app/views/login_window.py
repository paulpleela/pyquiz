# Form implementation generated from reading ui file 'login_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(950, 600)
        LoginWindow.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.gridLayout_2 = QtWidgets.QGridLayout(LoginWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(parent=LoginWindow)
        self.frame.setMaximumSize(QtCore.QSize(300, 400))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 271, 231))
        self.verticalLayoutWidget.setMinimumSize(QtCore.QSize(269, 24))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.title.setMinimumSize(QtCore.QSize(269, 24))
        self.title.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.frame_1 = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        self.frame_1.setMinimumSize(QtCore.QSize(269, 24))
        self.frame_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_1.setObjectName("frame_1")
        self.username_label = QtWidgets.QLabel(parent=self.frame_1)
        self.username_label.setGeometry(QtCore.QRect(0, 0, 269, 24))
        self.username_label.setMinimumSize(QtCore.QSize(269, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.username_input = QtWidgets.QLineEdit(parent=self.frame_1)
        self.username_input.setEnabled(True)
        self.username_input.setGeometry(QtCore.QRect(0, 20, 271, 24))
        self.username_input.setMinimumSize(QtCore.QSize(269, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.username_input.setFont(font)
        self.username_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.username_input.setObjectName("username_input")
        self.verticalLayout.addWidget(self.frame_1)
        self.frame_2 = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        self.frame_2.setMinimumSize(QtCore.QSize(269, 24))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.password_label = QtWidgets.QLabel(parent=self.frame_2)
        self.password_label.setGeometry(QtCore.QRect(0, 0, 269, 24))
        self.password_label.setMinimumSize(QtCore.QSize(269, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.password_input = QtWidgets.QLineEdit(parent=self.frame_2)
        self.password_input.setGeometry(QtCore.QRect(0, 20, 271, 24))
        self.password_input.setMinimumSize(QtCore.QSize(269, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_input.setFont(font)
        self.password_input.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhHiddenText|QtCore.Qt.InputMethodHint.ImhNoAutoUppercase|QtCore.Qt.InputMethodHint.ImhNoPredictiveText|QtCore.Qt.InputMethodHint.ImhSensitiveData)
        self.password_input.setText("")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_input.setObjectName("password_input")
        self.verticalLayout.addWidget(self.frame_2)
        self.login_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.login_button.setMinimumSize(QtCore.QSize(269, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.login_button.setFont(font)
        self.login_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.login_button.setObjectName("login_button")
        self.verticalLayout.addWidget(self.login_button)
        self.goto_register_button = QtWidgets.QPushButton(parent=self.frame)
        self.goto_register_button.setGeometry(QtCore.QRect(20, 250, 271, 24))
        self.goto_register_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.goto_register_button.setObjectName("goto_register_button")
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
        self.title.setText(_translate("LoginWindow", "Welcome"))
        self.username_label.setText(_translate("LoginWindow", "Username"))
        self.password_label.setText(_translate("LoginWindow", "Password"))
        self.login_button.setText(_translate("LoginWindow", "Log in"))
        self.goto_register_button.setText(_translate("LoginWindow", "Don\'t have an account? Register"))