# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Nust SE-12\3rd Semester\DataBase\project\UI\viewCustomerWindow.ui'
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
        Form.setStyleSheet("QLabel{\n"
"font-size: 15px\n"
"}\n"
"QHeaderView::section { color:white; background-color:#232326; }")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(510, 90, 131, 51))
        self.label.setStyleSheet("font: 700 9pt \"Arial\";\n"
"font-size: 15px;\n"
"color: white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(500, 120, 141, 41))
        self.label_2.setStyleSheet("font: 700 9pt \"Arial\";\n"
"font-size: 15px;\n"
"color: white;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(510, 140, 141, 41))
        self.label_3.setStyleSheet("font: 700 9pt \"Arial\";\n"
"font-size: 15px;\n"
"color: white;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(60, 110, 101, 21))
        self.label_4.setStyleSheet("font: 700 9pt \"Arial\";\n"
"font-size: 10px;\n"
"color: black;\n"
"background-color: rgb(47, 107, 100);")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(170, 110, 201, 24))
        self.lineEdit.setStyleSheet("background-color: rgb(252, 252, 252);")
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(670, 20, 72, 24))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(610, 20, 41, 21))
        self.label_5.setStyleSheet("font: 700 9pt \"Arial\";\n"
"font-size: 10px;\n"
"color: black;\n"
"background-color: rgb(47, 107, 100);")
        self.label_5.setObjectName("label_5")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 190, 711, 351))
        self.tableWidget.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"font: 700 9pt \"Segoe UI\";\n"
"\n"
"background-color: rgb(63, 63, 63);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(650, 105, 31, 21))
        self.label_6.setStyleSheet("font: 700 9pt \"Arial\";\n"
"font-size: 15px;\n"
"color: white;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(650, 130, 31, 16))
        self.label_7.setStyleSheet("font: 700 9pt \"Arial\";\n"
"font-size: 15px;\n"
"color: white;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(650, 155, 31, 21))
        self.label_8.setStyleSheet("font: 700 9pt \"Arial\";\n"
"font-size: 15px;\n"
"color: white;")
        self.label_8.setObjectName("label_8")
        self.prev_btn = QtWidgets.QPushButton(Form)
        self.prev_btn.setGeometry(QtCore.QRect(20, 20, 51, 21))
        self.prev_btn.setObjectName("prev_btn")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 761, 571))
        self.label_9.setStyleSheet("font: 8pt \"Segoe UI\";\n"
"font: 8pt \"Segoe UI\";\n"
"font: 11pt \"Segoe UI\";\n"
"color: black;")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("e:\\Nust SE-12\\3rd Semester\\DataBase\\project\\UI\\../assets/background-2.jpg"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(300, 10, 121, 41))
        self.label_10.setStyleSheet("\n"
"color: White;\n"
"background-color: transparent;\n"
"font-size: 25px")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(290, 10, 71, 71))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("D:/NUST/project/assets/IMS_logo.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(390, 110, 80, 21))
        self.pushButton.setObjectName("pushButton")
        self.app_btn = QtWidgets.QPushButton(Form)
        self.app_btn.setGeometry(QtCore.QRect(700, 50, 51, 21))
        self.app_btn.setObjectName("app_btn")
        self.label_9.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.lineEdit.raise_()
        self.comboBox.raise_()
        self.label_5.raise_()
        self.tableWidget.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.prev_btn.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.pushButton.raise_()
        self.app_btn.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Total Accounts:"))
        self.label_2.setText(_translate("Form", "Active Accounts:"))
        self.label_3.setText(_translate("Form", "Dead Accounts:"))
        self.label_4.setText(_translate("Form", " Search Account:"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Enter account number"))
        self.comboBox.setItemText(0, _translate("Form", "Total"))
        self.comboBox.setItemText(1, _translate("Form", "Active"))
        self.comboBox.setItemText(2, _translate("Form", "Dead"))
        self.label_5.setText(_translate("Form", " Filter:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "AccountNo"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "C_ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Product_Purchased"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Mobile_No"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Income"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Gender"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Status"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "PlaceOfWork"))
        self.label_6.setText(_translate("Form", "500"))
        self.label_7.setText(_translate("Form", "100"))
        self.label_8.setText(_translate("Form", "300"))
        self.prev_btn.setText(_translate("Form", "Prev"))
        self.label_10.setText(_translate("Form", "Accounts"))
        self.pushButton.setText(_translate("Form", "Search"))
        self.app_btn.setText(_translate("Form", "Apply"))
