# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Nust SE-12\3rd Semester\DataBase\project\UI\login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(763, 571)
        loginWindow.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"font-size: 24px;\n"
"background-color: white;\n"
"}\n"
"\n"
"#loginWindow {\n"
"background-color:rgb(70, 97, 132);\n"
"background-repeat: no-repeat; \n"
"background-position: center;\n"
"}\n"
"\n"
"QFrame{\n"
"background: #333;\n"
"}\n"
"\n"
"QPushButton{\n"
"background: black;\n"
"border-radius: 10px;\n"
"color: white\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: red;\n"
"background-color: #fc836e;\n"
"cursor:pointer\n"
"\n"
"}\n"
"")
        loginWindow.setWindowFilePath("")
        self.frame = QtWidgets.QFrame(loginWindow)
        self.frame.setGeometry(QtCore.QRect(180, 80, 381, 411))
        self.frame.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"background-color: rgb(0, 62, 90);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(38, 30, 227, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.494318 rgba(52, 97, 129, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"border-radius: 20px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 40, 161, 81))
        self.label.setStyleSheet("color:black;\n"
"font: 700 9pt \"Segoe UI\";\n"
"font-size: 30px;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(60, 350, 261, 51))
        self.pushButton.setStyleSheet("color:black;\n"
"font: 9pt \"Segoe UI\";\n"
"font-size: 24px;")
        self.pushButton.setObjectName("pushButton")
        self.user_name = QtWidgets.QLineEdit(self.frame)
        self.user_name.setGeometry(QtCore.QRect(40, 150, 321, 41))
        self.user_name.setStyleSheet("font: 9pt \"Arial\";\n"
"font-size: 20px;\n"
"background: white;\n"
"border: none;\n"
"color: #717072;\n"
"border-bottom: 1px solid rgb(119, 255, 173);\n"
"")
        self.user_name.setText("")
        self.user_name.setObjectName("user_name")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(40, 240, 321, 41))
        self.password.setStyleSheet("font: 9pt \"Arial\";\n"
"font-size: 20px;\n"
"background: white;\n"
"border: none;\n"
"color: #717072;\n"
"border-bottom: 1px solid rgb(119, 255, 173);\n"
"")
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.managerCheck = QtWidgets.QCheckBox(self.frame)
        self.managerCheck.setGeometry(QtCore.QRect(30, 300, 201, 31))
        self.managerCheck.setStyleSheet("font: 9pt \"Arial\";\n"
"font-size: 15px;\n"
"color: black;\n"
"background:transparent")
        self.managerCheck.setObjectName("managerCheck")
        self.label_2 = QtWidgets.QLabel(loginWindow)
        self.label_2.setGeometry(QtCore.QRect(350, 50, 61, 61))
        self.label_2.setStyleSheet("background-color: rgb(0, 48, 70);\n"
"")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("e:\\Nust SE-12\\3rd Semester\\DataBase\\project\\UI\\../assets/account.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(loginWindow)
        self.label_3.setGeometry(QtCore.QRect(330, 30, 101, 101))
        self.label_3.setStyleSheet("background-color: rgb(0, 48, 70);\n"
"border-radius: 50px;\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.backImage = QtWidgets.QLabel(loginWindow)
        self.backImage.setGeometry(QtCore.QRect(0, 0, 761, 571))
        self.backImage.setStyleSheet("background-color: white;background-color: rgb(0, 85, 127);\n"
"background-color: rgb(0, 62, 90);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(38, 30, 227, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.494318 rgba(52, 97, 129, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.backImage.setText("")
        self.backImage.setPixmap(QtGui.QPixmap("e:\\Nust SE-12\\3rd Semester\\DataBase\\project\\UI\\../assets/Background.jpg"))
        self.backImage.setScaledContents(True)
        self.backImage.setObjectName("backImage")
        self.label_4 = QtWidgets.QLabel(loginWindow)
        self.label_4.setGeometry(QtCore.QRect(40, 510, 231, 31))
        self.label_4.setStyleSheet("font-size: 15px;\n"
"color: red;\n"
"background:  transparent")
        self.label_4.setObjectName("label_4")
        self.backImage.raise_()
        self.frame.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.label_4.raise_()

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "Form"))
        self.label.setText(_translate("loginWindow", "    LOGIN"))
        self.pushButton.setText(_translate("loginWindow", "L O G I N"))
        self.user_name.setPlaceholderText(_translate("loginWindow", "User Name"))
        self.password.setPlaceholderText(_translate("loginWindow", "Password"))
        self.managerCheck.setText(_translate("loginWindow", "Are you a manager?"))
        self.label_4.setText(_translate("loginWindow", "Invalid login, please try again"))
