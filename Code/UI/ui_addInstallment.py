# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Nust SE-12\3rd Semester\DataBase\project\UI\addInstallment.ui'
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
        Form.setStyleSheet("QHeaderView::section { color:white; background-color:#232326; }\n"
"QLabel{font: 700 11pt \"Segoe UI\";}\n"
"")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 711, 511))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.search_btn1 = QtWidgets.QPushButton(self.tab)
        self.search_btn1.setGeometry(QtCore.QRect(600, 20, 75, 24))
        self.search_btn1.setStyleSheet("background-color: rgb(52, 156, 161);\n"
"font: 700 9pt \"Segoe UI\";\n"
"font-size: 13px;\n"
"color: black;")
        self.search_btn1.setObjectName("search_btn1")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(180, 10, 201, 41))
        self.label.setStyleSheet("\n"
"color: White;\n"
"background-color: transparent;\n"
"font-size: 25px")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(410, 20, 171, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(72, 72, 72);\n"
"color: white;")
        self.lineEdit.setObjectName("lineEdit")
        self.cus_Info = QtWidgets.QFrame(self.tab)
        self.cus_Info.setEnabled(True)
        self.cus_Info.setGeometry(QtCore.QRect(10, 70, 691, 411))
        self.cus_Info.setStyleSheet("border-top-color: rgb(250, 250, 250);\n"
"color: black;\n"
"QLabel{font: 700 11pt \"Segoe UI\";}")
        self.cus_Info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cus_Info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cus_Info.setObjectName("cus_Info")
        self.label_12 = QtWidgets.QLabel(self.cus_Info)
        self.label_12.setGeometry(QtCore.QRect(210, 91, 101, 31))
        self.label_12.setObjectName("label_12")
        self.label_10 = QtWidgets.QLabel(self.cus_Info)
        self.label_10.setGeometry(QtCore.QRect(200, 40, 171, 41))
        self.label_10.setObjectName("label_10")
        self.label_3 = QtWidgets.QLabel(self.cus_Info)
        self.label_3.setGeometry(QtCore.QRect(120, 70, 71, 21))
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.cus_Info)
        self.label_5.setGeometry(QtCore.QRect(390, 40, 131, 41))
        self.label_5.setStyleSheet("QLabel{font: 700 11pt \"Segoe UI\";}")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.cus_Info)
        self.label_6.setGeometry(QtCore.QRect(90, 90, 111, 31))
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.label_15 = QtWidgets.QLabel(self.cus_Info)
        self.label_15.setGeometry(QtCore.QRect(530, 50, 21, 21))
        self.label_15.setObjectName("label_15")
        self.label_11 = QtWidgets.QLabel(self.cus_Info)
        self.label_11.setGeometry(QtCore.QRect(410, 10, 141, 31))
        self.label_11.setStyleSheet("\n"
"font: 700 9pt \"Arial\";\n"
"font-size: 17px")
        self.label_11.setObjectName("label_11")
        self.label_4 = QtWidgets.QLabel(self.cus_Info)
        self.label_4.setGeometry(QtCore.QRect(130, 50, 61, 21))
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.label_18 = QtWidgets.QLabel(self.cus_Info)
        self.label_18.setGeometry(QtCore.QRect(530, 80, 21, 16))
        self.label_18.setObjectName("label_18")
        self.label_8 = QtWidgets.QLabel(self.cus_Info)
        self.label_8.setGeometry(QtCore.QRect(390, 70, 131, 31))
        self.label_8.setStyleSheet("QLabel{font: 700 11pt \"Segoe UI\";}")
        self.label_8.setObjectName("label_8")
        self.label_2 = QtWidgets.QLabel(self.cus_Info)
        self.label_2.setGeometry(QtCore.QRect(170, 10, 81, 31))
        self.label_2.setStyleSheet("\n"
"font: 700 11pt \"Arial\";\n"
"font-size: 17px")
        self.label_2.setObjectName("label_2")
        self.label_13 = QtWidgets.QLabel(self.cus_Info)
        self.label_13.setGeometry(QtCore.QRect(200, 70, 101, 21))
        self.label_13.setObjectName("label_13")
        self.tableWidget = QtWidgets.QTableWidget(self.cus_Info)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(10, 150, 681, 261))
        self.tableWidget.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"font: 700 9pt \"Segoe UI\";\n"
"\n"
"background-color: rgb(63, 63, 63);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.label_17 = QtWidgets.QLabel(self.cus_Info)
        self.label_17.setGeometry(QtCore.QRect(530, 100, 41, 21))
        self.label_17.setObjectName("label_17")
        self.label_9 = QtWidgets.QLabel(self.cus_Info)
        self.label_9.setGeometry(QtCore.QRect(420, 100, 91, 21))
        self.label_9.setStyleSheet("QLabel{font: 700 11pt \"Segoe UI\";}")
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(self.cus_Info)
        self.label_7.setGeometry(QtCore.QRect(70, 110, 131, 31))
        self.label_7.setStyleSheet("")
        self.label_7.setObjectName("label_7")
        self.label_14 = QtWidgets.QLabel(self.cus_Info)
        self.label_14.setGeometry(QtCore.QRect(210, 110, 71, 31))
        self.label_14.setObjectName("label_14")
        self.label_28 = QtWidgets.QLabel(self.cus_Info)
        self.label_28.setGeometry(QtCore.QRect(430, 120, 71, 21))
        self.label_28.setStyleSheet("QLabel{font: 700 11pt \"Segoe UI\";}")
        self.label_28.setObjectName("label_28")
        self.label_46 = QtWidgets.QLabel(self.cus_Info)
        self.label_46.setGeometry(QtCore.QRect(530, 120, 71, 21))
        self.label_46.setObjectName("label_46")
        self.label_22 = QtWidgets.QLabel(self.tab)
        self.label_22.setGeometry(QtCore.QRect(0, -30, 711, 521))
        self.label_22.setStyleSheet("background-color: rgb(72, 72, 72);\n"
"color: white;")
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("e:\\Nust SE-12\\3rd Semester\\DataBase\\project\\UI\\../assets/background-2.jpg"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.tab)
        self.label_23.setGeometry(QtCore.QRect(136, 10, 41, 41))
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("e:\\Nust SE-12\\3rd Semester\\DataBase\\project\\UI\\../assets/IMS_logo.png"))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")
        self.Home5 = QtWidgets.QPushButton(self.tab)
        self.Home5.setGeometry(QtCore.QRect(10, 10, 51, 21))
        self.Home5.setStyleSheet("background-color: rgb(52, 156, 161);\n"
"font: 700 9pt \"Segoe UI\";\n"
"font-size: 13px;\n"
"color: black;")
        self.Home5.setObjectName("Home5")
        self.label_22.raise_()
        self.search_btn1.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.cus_Info.raise_()
        self.label_23.raise_()
        self.Home5.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(280, 20, 191, 31))
        self.label_16.setStyleSheet("\n"
"color: White;\n"
"background-color: transparent;\n"
"font-size: 25px")
        self.label_16.setObjectName("label_16")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(210, 140, 101, 21))
        self.label_19.setStyleSheet("background-color: rgb(47, 107, 100);\n"
"font: 700 9pt \"Arial\";\n"
"font-size: 15px;\n"
"color: black;")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(210, 190, 61, 21))
        self.label_20.setStyleSheet("background-color: rgb(47, 107, 100);\n"
"font: 700 9pt \"Arial\";\n"
"font-size: 15px;\n"
"color: black;")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setGeometry(QtCore.QRect(210, 240, 71, 21))
        self.label_21.setStyleSheet("background-color: rgb(47, 107, 100);\n"
"font: 700 9pt \"Arial\";\n"
"font-size: 15px;\n"
"color: black;")
        self.label_21.setObjectName("label_21")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 140, 161, 22))
        self.lineEdit_2.setStyleSheet("background-color: white;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(320, 190, 161, 22))
        self.lineEdit_3.setStyleSheet("background-color: white;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(320, 240, 161, 22))
        self.lineEdit_4.setStyleSheet("background-color: white;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 320, 80, 24))
        self.pushButton_3.setStyleSheet("background-color: rgb(52, 156, 161);\n"
"font: 700 9pt \"Arial\";\n"
"font-size: 10px;\n"
"color: black;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setGeometry(QtCore.QRect(80, 70, 711, 511))
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setGeometry(QtCore.QRect(0, 0, 761, 571))
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("e:\\Nust SE-12\\3rd Semester\\DataBase\\project\\UI\\../assets/background-2.jpg"))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setGeometry(QtCore.QRect(220, 10, 51, 51))
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap("e:\\Nust SE-12\\3rd Semester\\DataBase\\project\\UI\\../assets/IMS_logo.png"))
        self.label_26.setScaledContents(True)
        self.label_26.setObjectName("label_26")
        self.Home6 = QtWidgets.QPushButton(self.tab_2)
        self.Home6.setGeometry(QtCore.QRect(0, 10, 51, 21))
        self.Home6.setStyleSheet("background-color: rgb(72, 72, 72);\n"
"color: white;")
        self.Home6.setObjectName("Home6")
        self.newPrev = QtWidgets.QPushButton(self.tab_2)
        self.newPrev.setGeometry(QtCore.QRect(50, 320, 80, 24))
        self.newPrev.setStyleSheet("background-color: rgb(52, 156, 161);\n"
"font: 700 9pt \"Arial\";\n"
"font-size: 10px;\n"
"color: black;")
        self.newPrev.setObjectName("newPrev")
        self.label_25.raise_()
        self.label_24.raise_()
        self.label_16.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.pushButton_3.raise_()
        self.label_26.raise_()
        self.Home6.raise_()
        self.newPrev.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.addInstallementButton = QtWidgets.QPushButton(Form)
        self.addInstallementButton.setGeometry(QtCore.QRect(560, 530, 171, 31))
        self.addInstallementButton.setStyleSheet("background-color: rgb(52, 156, 161);\n"
"font: 600 9pt \"Segoe UI\";\n"
"font-size: 13px;\n"
"color: black;")
        self.addInstallementButton.setObjectName("addInstallementButton")
        self.label_27 = QtWidgets.QLabel(Form)
        self.label_27.setGeometry(QtCore.QRect(0, -10, 761, 591))
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap("e:\\Nust SE-12\\3rd Semester\\DataBase\\project\\UI\\../assets/background-1.jpg"))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.label_27.raise_()
        self.tabWidget.raise_()
        self.addInstallementButton.raise_()

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.search_btn1.setText(_translate("Form", "Search"))
        self.label.setText(_translate("Form", "Search Customer"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Enter Account Number"))
        self.label_12.setText(_translate("Form", "50000"))
        self.label_10.setText(_translate("Form", "Muhammad Yameen"))
        self.label_3.setText(_translate("Form", "Product:"))
        self.label_5.setText(_translate("Form", "Total installment:"))
        self.label_6.setText(_translate("Form", "Total amount:"))
        self.label_15.setText(_translate("Form", "8"))
        self.label_11.setText(_translate("Form", "   Installments:"))
        self.label_4.setText(_translate("Form", "Name:"))
        self.label_18.setText(_translate("Form", "6"))
        self.label_8.setText(_translate("Form", "Paid installment:"))
        self.label_2.setText(_translate("Form", " Details:"))
        self.label_13.setText(_translate("Form", "Mobile"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Installment No"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "AmountPaid"))
        self.label_17.setText(_translate("Form", "3"))
        self.label_9.setText(_translate("Form", "Remaining:"))
        self.label_7.setText(_translate("Form", "Remaing amount:"))
        self.label_14.setText(_translate("Form", "30000"))
        self.label_28.setText(_translate("Form", "Amount:"))
        self.label_46.setText(_translate("Form", "0"))
        self.Home5.setText(_translate("Form", "Home"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.label_16.setText(_translate("Form", "Add Installment"))
        self.label_19.setText(_translate("Form", " Account No:"))
        self.label_20.setText(_translate("Form", " Date:"))
        self.label_21.setText(_translate("Form", " Amount:"))
        self.pushButton_3.setText(_translate("Form", "Add"))
        self.Home6.setText(_translate("Form", "Home"))
        self.newPrev.setText(_translate("Form", "Prev"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))
        self.addInstallementButton.setText(_translate("Form", "Add New Installment"))