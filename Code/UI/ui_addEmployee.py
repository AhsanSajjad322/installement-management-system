# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Nust SE-12\3rd Semester\DataBase\project\UI\addEmployee.ui'
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
        Form.setStyleSheet("Qlabel{ color: black\n"
"}\n"
"\n"
"QLineEdit{\n"
"background: rgb(197, 197, 197);\n"
"border-radius:5px;\n"
"font: 11pt \"Segoe UI\";\n"
"}\n"
"QComboBox{\n"
"background: rgb(139, 139, 139)\n"
"\n"
"}")
        self.last_name = QtWidgets.QLineEdit(Form)
        self.last_name.setGeometry(QtCore.QRect(510, 140, 181, 31))
        self.last_name.setObjectName("last_name")
        self.e_phone = QtWidgets.QLabel(Form)
        self.e_phone.setGeometry(QtCore.QRect(50, 300, 91, 21))
        self.e_phone.setStyleSheet("\n"
"font: 700 9pt \"Segoe UI\";\n"
"font-size: 17px;\n"
"color:black;")
        self.e_phone.setObjectName("e_phone")
        self.father_name = QtWidgets.QLineEdit(Form)
        self.father_name.setGeometry(QtCore.QRect(510, 190, 181, 31))
        self.father_name.setObjectName("father_name")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(380, 200, 121, 21))
        self.label_6.setStyleSheet("\n"
"font: 700 9pt \"Segoe UI\";\n"
"font-size: 17px;\n"
"color:black;")
        self.label_6.setObjectName("label_6")
        self.first_name = QtWidgets.QLineEdit(Form)
        self.first_name.setGeometry(QtCore.QRect(150, 140, 181, 31))
        self.first_name.setStyleSheet("")
        self.first_name.setText("")
        self.first_name.setObjectName("first_name")
        self.e_works_hours = QtWidgets.QLabel(Form)
        self.e_works_hours.setGeometry(QtCore.QRect(30, 410, 101, 21))
        self.e_works_hours.setStyleSheet("\n"
"font: 700 9pt \"Segoe UI\";\n"
"font-size: 17px;\n"
"color:black;")
        self.e_works_hours.setObjectName("e_works_hours")
        self.e_designation = QtWidgets.QLabel(Form)
        self.e_designation.setGeometry(QtCore.QRect(390, 300, 101, 31))
        self.e_designation.setStyleSheet("\n"
"font: 700 9pt \"Segoe UI\";\n"
"font-size: 17px;\n"
"color:black;")
        self.e_designation.setObjectName("e_designation")
        self.e_cnic = QtWidgets.QLabel(Form)
        self.e_cnic.setGeometry(QtCore.QRect(20, 190, 121, 21))
        self.e_cnic.setStyleSheet("\n"
"font: 700 9pt \"Segoe UI\";\n"
"font-size: 17px;\n"
"color:black;")
        self.e_cnic.setObjectName("e_cnic")
        self.e_first_name = QtWidgets.QLabel(Form)
        self.e_first_name.setGeometry(QtCore.QRect(40, 140, 101, 21))
        self.e_first_name.setStyleSheet("\n"
"font: 700 9pt \"Segoe UI\";\n"
"font-size: 17px;\n"
"color:black;")
        self.e_first_name.setObjectName("e_first_name")
        self.e_last_name = QtWidgets.QLabel(Form)
        self.e_last_name.setGeometry(QtCore.QRect(380, 150, 91, 21))
        self.e_last_name.setStyleSheet("\n"
"font: 700 9pt \"Segoe UI\";\n"
"font-size: 17px;\n"
"color:black;")
        self.e_last_name.setObjectName("e_last_name")
        self.dob = QtWidgets.QLineEdit(Form)
        self.dob.setGeometry(QtCore.QRect(150, 250, 181, 31))
        self.dob.setText("")
        self.dob.setObjectName("dob")
        self.e_gender = QtWidgets.QLabel(Form)
        self.e_gender.setGeometry(QtCore.QRect(410, 250, 71, 21))
        self.e_gender.setStyleSheet("\n"
"font: 700 9pt \"Segoe UI\";\n"
"font-size: 17px;\n"
"color:black;")
        self.e_gender.setObjectName("e_gender")
        self.phone = QtWidgets.QLineEdit(Form)
        self.phone.setGeometry(QtCore.QRect(150, 300, 181, 31))
        self.phone.setObjectName("phone")
        self.address = QtWidgets.QLineEdit(Form)
        self.address.setGeometry(QtCore.QRect(510, 350, 181, 31))
        self.address.setObjectName("address")
        self.salary = QtWidgets.QLineEdit(Form)
        self.salary.setGeometry(QtCore.QRect(510, 410, 181, 31))
        self.salary.setObjectName("salary")
        self.e_salary = QtWidgets.QLabel(Form)
        self.e_salary.setGeometry(QtCore.QRect(440, 410, 61, 21))
        self.e_salary.setStyleSheet("\n"
"font: 700 9pt \"Segoe UI\";\n"
"font-size: 17px;\n"
"color:black;")
        self.e_salary.setObjectName("e_salary")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(270, 20, 311, 51))
        self.label_3.setStyleSheet("\n"
"color: white;\n"
"font: 700 9pt \"Segoe UI\";\n"
"background-color: transparent;\n"
"font-size: 28px")
        self.label_3.setObjectName("label_3")
        self.e_martial_status = QtWidgets.QLabel(Form)
        self.e_martial_status.setGeometry(QtCore.QRect(30, 360, 121, 21))
        self.e_martial_status.setStyleSheet("\n"
"font: 700 9pt \"Segoe UI\";\n"
"font-size: 17px;\n"
"color:black;")
        self.e_martial_status.setObjectName("e_martial_status")
        self.work_hours = QtWidgets.QLineEdit(Form)
        self.work_hours.setGeometry(QtCore.QRect(150, 410, 181, 31))
        self.work_hours.setObjectName("work_hours")
        self.e_dob = QtWidgets.QLabel(Form)
        self.e_dob.setGeometry(QtCore.QRect(30, 250, 111, 21))
        self.e_dob.setStyleSheet("\n"
"font: 700 9pt \"Segoe UI\";\n"
"font-size: 17px;\n"
"color:black;")
        self.e_dob.setObjectName("e_dob")
        self.e_address = QtWidgets.QLabel(Form)
        self.e_address.setGeometry(QtCore.QRect(430, 360, 81, 21))
        self.e_address.setStyleSheet("\n"
"font: 700 9pt \"Segoe UI\";\n"
"font-size: 17px;\n"
"color:black;")
        self.e_address.setObjectName("e_address")
        self.cnic = QtWidgets.QLineEdit(Form)
        self.cnic.setGeometry(QtCore.QRect(150, 190, 181, 31))
        self.cnic.setObjectName("cnic")
        self.add_btn = QtWidgets.QPushButton(Form)
        self.add_btn.setGeometry(QtCore.QRect(630, 510, 80, 24))
        self.add_btn.setStyleSheet("font: 700 9pt \"Segoe UI\";")
        self.add_btn.setObjectName("add_btn")
        self.prev_btn = QtWidgets.QPushButton(Form)
        self.prev_btn.setGeometry(QtCore.QRect(10, 10, 51, 21))
        self.prev_btn.setStyleSheet("font: 700 9pt \"Segoe UI\";")
        self.prev_btn.setObjectName("prev_btn")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(510, 250, 81, 31))
        self.comboBox.setStyleSheet("font: 700 9pt \"Segoe UI\";\n"
"font-size: 15 px;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(510, 300, 131, 31))
        self.comboBox_2.setStyleSheet("font: 700 9pt \"Segoe UI\";\n"
"background: grey")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(160, 350, 121, 31))
        self.comboBox_3.setStyleSheet("font: 700 9pt \"Segoe UI\";\n"
"font: 11pt \"Segoe UI\";\n"
"font: 700 10pt \"Segoe UI\";\n"
"font-size: 15 px;")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 761, 571))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("e:\\Nust SE-12\\3rd Semester\\DataBase\\project\\UI\\../assets/background-2.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 81, 81))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("e:\\Nust SE-12\\3rd Semester\\DataBase\\project\\UI\\../NUST/project/assets/IMS_logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.last_name.raise_()
        self.e_phone.raise_()
        self.father_name.raise_()
        self.label_6.raise_()
        self.first_name.raise_()
        self.e_works_hours.raise_()
        self.e_designation.raise_()
        self.e_cnic.raise_()
        self.e_first_name.raise_()
        self.e_last_name.raise_()
        self.dob.raise_()
        self.e_gender.raise_()
        self.phone.raise_()
        self.address.raise_()
        self.salary.raise_()
        self.e_salary.raise_()
        self.label_3.raise_()
        self.e_martial_status.raise_()
        self.work_hours.raise_()
        self.e_dob.raise_()
        self.e_address.raise_()
        self.cnic.raise_()
        self.add_btn.raise_()
        self.prev_btn.raise_()
        self.comboBox.raise_()
        self.comboBox_2.raise_()
        self.comboBox_3.raise_()
        self.label_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.e_phone.setText(_translate("Form", "Phone No:"))
        self.label_6.setText(_translate("Form", "Father\'s Name:"))
        self.e_works_hours.setText(_translate("Form", "Work Hours:"))
        self.e_designation.setText(_translate("Form", "Designation:"))
        self.e_cnic.setText(_translate("Form", "CNIC Number:"))
        self.e_first_name.setText(_translate("Form", "First Name:"))
        self.e_last_name.setText(_translate("Form", "Last Name:"))
        self.e_gender.setText(_translate("Form", "Gender:"))
        self.e_salary.setText(_translate("Form", "Salary:"))
        self.label_3.setText(_translate("Form", "Employee Information"))
        self.e_martial_status.setText(_translate("Form", "Martial Status:"))
        self.e_dob.setText(_translate("Form", "Date of Birth:"))
        self.e_address.setText(_translate("Form", "Address:"))
        self.add_btn.setText(_translate("Form", "Add"))
        self.prev_btn.setText(_translate("Form", "Prev"))
        self.comboBox.setItemText(0, _translate("Form", "M"))
        self.comboBox.setItemText(1, _translate("Form", "F"))
        self.comboBox.setItemText(2, _translate("Form", "other"))
        self.comboBox_2.setItemText(0, _translate("Form", "Operator"))
        self.comboBox_2.setItemText(1, _translate("Form", "Recover_Collector"))
        self.comboBox_3.setItemText(0, _translate("Form", "Married"))
        self.comboBox_3.setItemText(1, _translate("Form", "Single"))
