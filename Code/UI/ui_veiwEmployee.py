# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Nust SE-12\3rd Semester\DataBase\project\UI\veiwEmployee.ui'
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
        Form.setStyleSheet("QHeaderView::section { color:white; background-color:#232326; }")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(20, 30, 711, 511))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(130, 150, 81, 41))
        self.label_3.setStyleSheet("font: 700 9pt \"Arial\";\n"
"font-size: 14px;\n"
"color: white;")
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 190, 711, 281))
        self.tableWidget.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"font: 700 9pt \"Segoe UI\";\n"
"background-color: rgb(63, 63, 63);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(13)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.verticalHeader().setVisible(False)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(80, 110, 131, 41))
        self.label.setStyleSheet("font: 700 9pt \"Arial\";\n"
"font-size: 14px;\n"
"color: white;")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(620, 20, 72, 24))
        self.comboBox.setStyleSheet("background-color: rgb(105, 105, 105);\n"
"background-color: rgb(73, 73, 73);\n"
"font: 700 9pt \"Arial\";\n"
"font-size: 12px;\n"
"color: white;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(560, 20, 51, 21))
        self.label_5.setStyleSheet("font: 700 9pt \"Arial\";\n"
"font-size: 12px;\n"
"color: white;\n"
"background-color: rgb(47, 107, 100);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(230, 120, 16, 21))
        self.label_6.setStyleSheet("font: 700 9pt \"Arial\";\n"
"font-size: 15px;\n"
"color: white;")
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 161, 41))
        self.label_2.setStyleSheet("font: 700 9pt \"Arial\";\n"
"font-size: 14px;\n"
"color: white;")
        self.label_2.setObjectName("label_2")
        self.id_entered = QtWidgets.QLineEdit(self.tab)
        self.id_entered.setGeometry(QtCore.QRect(150, 80, 131, 24))
        self.id_entered.setObjectName("id_entered")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(230, 140, 21, 21))
        self.label_7.setStyleSheet("font: 700 9pt \"Arial\";\n"
"font-size: 15px;\n"
"color: white;")
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 131, 21))
        self.label_4.setStyleSheet("background-color: rgb(47, 107, 100);\n"
"font: 700 9pt \"Arial\";\n"
"font-size: 11px;\n"
"color: white;")
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(230, 160, 21, 21))
        self.label_8.setStyleSheet("font: 700 9pt \"Arial\";\n"
"font-size: 15px;\n"
"color: white;")
        self.label_8.setObjectName("label_8")
        self.search_btn = QtWidgets.QPushButton(self.tab)
        self.search_btn.setGeometry(QtCore.QRect(290, 80, 80, 24))
        self.search_btn.setStyleSheet("background-color: rgb(105, 105, 105);\n"
"background-color: rgb(73, 73, 73);\n"
"font: 700 9pt \"Arial\";\n"
"font-size: 12px;\n"
"color: white;")
        self.search_btn.setObjectName("search_btn")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(390, 140, 221, 21))
        self.label_9.setStyleSheet("background-color: rgb(47, 107, 100);\n"
"font: 700 9pt \"Arial\";\n"
"font-size: 11px;\n"
"color: white;")
        self.label_9.setObjectName("label_9")
        self.view_btn = QtWidgets.QPushButton(self.tab)
        self.view_btn.setGeometry(QtCore.QRect(620, 140, 80, 24))
        self.view_btn.setStyleSheet("background-color: rgb(105, 105, 105);\n"
"background-color: rgb(73, 73, 73);\n"
"font: 700 9pt \"Arial\";\n"
"font-size: 12px;\n"
"color: white;")
        self.view_btn.setObjectName("view_btn")
        self.prev_btn = QtWidgets.QPushButton(self.tab)
        self.prev_btn.setGeometry(QtCore.QRect(0, 0, 31, 21))
        self.prev_btn.setStyleSheet("background-color: rgb(105, 105, 105);\n"
"background-color: rgb(73, 73, 73);\n"
"font: 700 9pt \"Arial\";\n"
"font-size: 12px;\n"
"color: white;")
        self.prev_btn.setObjectName("prev_btn")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(40, 711, 511, 12))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("D:/3RD SEMESTER/DatabaseSystems/Lectures/background-2.jpg"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(0, 0, 711, 511))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("e:\\Nust SE-12\\3rd Semester\\DataBase\\project\\UI\\../assets/background-2.jpg"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(350, 10, 121, 41))
        self.label_16.setStyleSheet("\n"
"color: White;\n"
"background-color: transparent;\n"
"font-size: 25px")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(290, 10, 51, 51))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("e:\\Nust SE-12\\3rd Semester\\DataBase\\project\\UI\\../assets/IMS_logo.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.apply_btn = QtWidgets.QPushButton(self.tab)
        self.apply_btn.setGeometry(QtCore.QRect(650, 50, 41, 21))
        self.apply_btn.setStyleSheet("background-color: rgb(105, 105, 105);\n"
"background-color: rgb(73, 73, 73);\n"
"font: 700 9pt \"Arial\";\n"
"font-size: 12px;\n"
"color: white;")
        self.apply_btn.setObjectName("apply_btn")
        self.label_15.raise_()
        self.label_3.raise_()
        self.tableWidget.raise_()
        self.label.raise_()
        self.comboBox.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_2.raise_()
        self.id_entered.raise_()
        self.label_7.raise_()
        self.label_4.raise_()
        self.label_8.raise_()
        self.search_btn.raise_()
        self.label_9.raise_()
        self.view_btn.raise_()
        self.prev_btn.raise_()
        self.label_14.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.apply_btn.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.search_btn1 = QtWidgets.QPushButton(self.tab_2)
        self.search_btn1.setGeometry(QtCore.QRect(310, 90, 75, 24))
        self.search_btn1.setStyleSheet("background-color: rgb(105, 105, 105);\n"
"background-color: rgb(73, 73, 73);\n"
"font: 700 9pt \"Arial\";\n"
"font-size: 12px;\n"
"color: white;")
        self.search_btn1.setObjectName("search_btn1")
        self.eId_Entered = QtWidgets.QLineEdit(self.tab_2)
        self.eId_Entered.setGeometry(QtCore.QRect(170, 90, 131, 21))
        self.eId_Entered.setObjectName("eId_Entered")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(40, 90, 121, 21))
        self.label_10.setStyleSheet("background-color: rgb(47, 107, 100);\n"
"font: 700 9pt \"Arial\";\n"
"font-size: 12px;\n"
"color: white;")
        self.label_10.setObjectName("label_10")
        self.b_btn = QtWidgets.QPushButton(self.tab_2)
        self.b_btn.setGeometry(QtCore.QRect(10, 10, 51, 21))
        self.b_btn.setStyleSheet("background-color: rgb(105, 105, 105);\n"
"background-color: rgb(73, 73, 73);\n"
"font: 700 9pt \"Arial\";\n"
"font-size: 12px;\n"
"color: white;")
        self.b_btn.setObjectName("b_btn")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(0, 0, 711, 511))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("e:\\Nust SE-12\\3rd Semester\\DataBase\\project\\UI\\../assets/background-2.jpg"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(330, 20, 121, 41))
        self.label_19.setStyleSheet("\n"
"color: White;\n"
"background-color: transparent;\n"
"font-size: 25px")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(260, 10, 61, 61))
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("e:\\Nust SE-12\\3rd Semester\\DataBase\\project\\UI\\../assets/IMS_logo.png"))
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")
        self.frame = QtWidgets.QFrame(self.tab_2)
        self.frame.setGeometry(QtCore.QRect(10, 140, 691, 341))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 30, 711, 301))
        self.tableWidget_2.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"font: 700 9pt \"Segoe UI\";\n"
"background-color: rgb(63, 63, 63);")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(8)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(140)
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(40, -10, 121, 41))
        self.label_12.setStyleSheet("font: 700 9pt \"Arial\";\n"
"font-size: 15px;\n"
"color: white;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(170, 0, 21, 21))
        self.label_13.setStyleSheet("font: 700 9pt \"Arial\";\n"
"font-size: 15px;\n"
"color: white;")
        self.label_13.setObjectName("label_13")
        self.label_18.raise_()
        self.search_btn1.raise_()
        self.eId_Entered.raise_()
        self.label_10.raise_()
        self.b_btn.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.frame.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(0, -10, 761, 581))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("e:\\Nust SE-12\\3rd Semester\\DataBase\\project\\UI\\../assets/background-1.jpg"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_11.raise_()
        self.tabWidget.raise_()

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Operators:"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "E_ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "M_ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "CNIC"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Father Name"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Phone"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Address"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "DOB"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Gender"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Form", "Designation"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Form", "WorksHours"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Form", "Salary"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("Form", "Martial Status"))
        self.label.setText(_translate("Form", "Total Employees:"))
        self.comboBox.setItemText(0, _translate("Form", "Total"))
        self.comboBox.setItemText(1, _translate("Form", "Recovery collectors"))
        self.comboBox.setItemText(2, _translate("Form", "Operators"))
        self.label_5.setText(_translate("Form", " Filter:"))
        self.label_6.setText(_translate("Form", "6"))
        self.label_2.setText(_translate("Form", "Recovery Collectors:"))
        self.id_entered.setPlaceholderText(_translate("Form", "Enter employee ID"))
        self.label_7.setText(_translate("Form", "4"))
        self.label_4.setText(_translate("Form", " Search Employee:"))
        self.label_8.setText(_translate("Form", "2"))
        self.search_btn.setText(_translate("Form", "Search"))
        self.label_9.setText(_translate("Form", " View Customers Under Employee:"))
        self.view_btn.setText(_translate("Form", "View"))
        self.prev_btn.setText(_translate("Form", "<"))
        self.label_16.setText(_translate("Form", "Employees"))
        self.apply_btn.setText(_translate("Form", "Apply"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.search_btn1.setText(_translate("Form", "Search"))
        self.eId_Entered.setPlaceholderText(_translate("Form", "Enter E_ID"))
        self.label_10.setText(_translate("Form", " Search Employee:"))
        self.b_btn.setText(_translate("Form", "prev"))
        self.label_19.setText(_translate("Form", "Employees"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Account_No"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Name"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Product_Purchased"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Total amount"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Amount paid"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Installment"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Total installements"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("Form", "InstallmentRemaing"))
        self.label_12.setText(_translate("Form", "Total Customers:"))
        self.label_13.setText(_translate("Form", "6"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))
