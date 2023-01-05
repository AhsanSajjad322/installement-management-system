# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Nust SE-12\3rd Semester\DataBase\project\UI\opretorWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(761, 571)
        self.addNewCustomer = QtWidgets.QPushButton(Form)
        self.addNewCustomer.setGeometry(QtCore.QRect(340, 280, 151, 41))
        self.addNewCustomer.setStyleSheet("font: 700 9pt \"Arial\";\n"
"font-size: 10px;\n"
"background-color: rgb(41, 103, 93);\n"
"font: 700 9pt \"Arial\";\n"
"font-size: 12px;\n"
"color: white;\n"
"font: 12pt \"Segoe UI\";\n"
"")
        self.addNewCustomer.setObjectName("addNewCustomer")
        self.addInstallment = QtWidgets.QPushButton(Form)
        self.addInstallment.setGeometry(QtCore.QRect(340, 380, 151, 41))
        self.addInstallment.setStyleSheet("font: 700 9pt \"Arial\";\n"
"font-size: 10px;\n"
"background-color: rgb(41, 103, 93);\n"
"font: 700 9pt \"Arial\";\n"
"font-size: 12px;\n"
"color: white;\n"
"font: 12pt \"Segoe UI\";\n"
"")
        self.addInstallment.setObjectName("addInstallment")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-20, -40, 831, 611))
        self.label.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"background-color: rgb(0, 62, 90);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(38, 30, 227, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.494318 rgba(52, 97, 129, 255), stop:1 rgba(255, 255, 255, 255));\n"
" QLabel{\n"
"color: white\n"
"\n"
"}")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/FAAAST 4/Desktop/assets/Background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(120, 30, 121, 121))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/FAAAST 4/Desktop/assets/IMS_logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(300, 210, 191, 21))
        self.label_3.setStyleSheet("font: 9pt \"Arial\";\n"
"font-size: 16px;\n"
"background-color: transparent;\n"
"color: white\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(310, 350, 251, 16))
        self.label_4.setStyleSheet("font: 9pt \"Arial\";\n"
"font-size: 16px;\n"
"background-color: transparent;\n"
"color: white")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(250, 200, 51, 51))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("e:\\Nust SE-12\\3rd Semester\\DataBase\\project\\UI\\../assets/customer.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(260, 340, 41, 41))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("e:\\Nust SE-12\\3rd Semester\\DataBase\\project\\UI\\../assets/Add_Installment.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(240, 330, 41, 41))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("C:/Users/FAAAST 4/Desktop/assets/New_account.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(260, 60, 281, 61))
        self.label_9.setStyleSheet("font-size: 50px;\n"
"color: White;\n"
"background-color: transparent;\n"
"")
        self.label_9.setObjectName("label_9")
        self.comboCustomer = QtWidgets.QComboBox(Form)
        self.comboCustomer.setGeometry(QtCore.QRect(380, 240, 101, 21))
        self.comboCustomer.setStyleSheet("font: 700 9pt \"Arial\";\n"
"font-size: 10px;\n"
"background-color: rgb(41, 103, 93);\n"
"color: white;\n"
"font: 9pt \"Segoe UI\";\n"
"")
        self.comboCustomer.setObjectName("comboCustomer")
        self.comboCustomer.addItem("")
        self.comboCustomer.addItem("")
        self.signOut_btn = QtWidgets.QPushButton(Form)
        self.signOut_btn.setGeometry(QtCore.QRect(700, 10, 51, 21))
        self.signOut_btn.setStyleSheet("background-color: rgb(41, 103, 93);\n"
"color: white;\n"
"font: 8pt \"Segoe UI\";\n"
"\n"
"")
        self.signOut_btn.setObjectName("signOut_btn")
        self.label.raise_()
        self.addNewCustomer.raise_()
        self.addInstallment.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_6.raise_()
        self.label_8.raise_()
        self.label_7.raise_()
        self.label_9.raise_()
        self.comboCustomer.raise_()
        self.signOut_btn.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.addNewCustomer.setText(_translate("Form", "Create Account"))
        self.addInstallment.setText(_translate("Form", "Add installment"))
        self.label_3.setText(_translate("Form", "Create a new Account!"))
        self.label_4.setText(_translate("Form", "To Add Installment Click Here!"))
        self.label_9.setText(_translate("Form", "Welcome!"))
        self.comboCustomer.setCurrentText(_translate("Form", "New Customer"))
        self.comboCustomer.setItemText(0, _translate("Form", "New Customer"))
        self.comboCustomer.setItemText(1, _translate("Form", "Existing Customer"))
        self.signOut_btn.setText(_translate("Form", "Log out"))
