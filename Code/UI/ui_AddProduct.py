# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Nust SE-12\3rd Semester\DataBase\project\UI\AddProduct.ui'
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
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 721, 511))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(50, 110, 121, 21))
        self.label.setStyleSheet("background-color: rgb(47, 107, 100);\n"
"font: 700 9pt \"Arial\";\n"
"font-size: 16px;\n"
"color: black")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(190, 110, 63, 20))
        self.label_2.setStyleSheet("font: 700 9pt \"Arial\";\n"
"font-size: 13px;\n"
"color: black")
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 140, 761, 301))
        self.tableWidget.setStyleSheet("background-color: rgb(249, 249, 249);\n"
"font: 700 9pt \"Segoe UI\";\n"
"font-size: 11px\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(77, 77, 77))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(77, 77, 77))
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(77, 77, 77))
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(1022, 510, 171, 29))
        self.pushButton.setObjectName("pushButton")
        self.prev_btn = QtWidgets.QPushButton(self.tab)
        self.prev_btn.setGeometry(QtCore.QRect(10, 10, 51, 21))
        self.prev_btn.setStyleSheet("background-color: rgb(105, 105, 105);\n"
"background-color: rgb(73, 73, 73);\n"
"\n"
"font: 700 9pt \"Segoe UI\";\n"
"font-size: 11px")
        self.prev_btn.setObjectName("prev_btn")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 761, 531))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("C:/Users/FAAAST 4/Desktop/assets/background-2.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(350, 30, 151, 41))
        self.label_8.setStyleSheet("font: 700 9pt \"Segoe UI\";\n"
"color: White;\n"
"background-color: transparent;\n"
"font-size: 25px")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(250, 10, 91, 81))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("C:/Users/FAAAST 4/Desktop/assets/IMS_logo.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.addNew_btn = QtWidgets.QPushButton(self.tab)
        self.addNew_btn.setGeometry(QtCore.QRect(569, 450, 131, 21))
        self.addNew_btn.setStyleSheet("background-color: rgb(46, 183, 183);\n"
"background-color: rgb(53, 184, 169);\n"
"background-color: rgb(53, 138, 125);\n"
"font: 700 9pt \"Segoe UI\";\n"
"color:black;\n"
"font-size: 11px\n"
"")
        self.addNew_btn.setObjectName("addNew_btn")
        self.label_6.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.tableWidget.raise_()
        self.pushButton.raise_()
        self.prev_btn.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.addNew_btn.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(190, 150, 121, 20))
        self.label_3.setStyleSheet("background-color: rgb(47, 107, 100);\n"
"font: 700 9pt \"Arial\";\n"
"font-size: 15px;\n"
"color: black;")
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(330, 150, 171, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(190, 210, 101, 20))
        self.label_4.setStyleSheet("background-color: rgb(47, 107, 100);\n"
"font: 700 9pt \"Arial\";\n"
"font-size: 15px;\n"
"color: black;")
        self.label_4.setObjectName("label_4")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_2.setGeometry(QtCore.QRect(330, 210, 171, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(190, 270, 63, 20))
        self.label_5.setStyleSheet("background-color: rgb(47, 107, 100);\n"
"font: 700 9pt \"Arial\";\n"
"font-size: 15px;\n"
"color: black;")
        self.label_5.setObjectName("label_5")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_3.setGeometry(QtCore.QRect(330, 270, 171, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 380, 83, 29))
        self.pushButton_2.setStyleSheet("background-color: rgb(52, 156, 161);\n"
"font: 700 9pt \"Segoe UI\";\n"
"font-size: 13px;\n"
"color: black;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 721, 511))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("C:/Users/FAAAST 4/Desktop/assets/background-2.jpg"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(500, 320, 37, 12))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(350, 30, 161, 41))
        self.label_12.setStyleSheet("font: 700 9pt \"Segoe UI\";\n"
"color: White;\n"
"background-color: transparent;\n"
"font-size: 25px")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(250, 10, 91, 81))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("C:/Users/FAAAST 4/Desktop/assets/IMS_logo.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 10, 31, 21))
        self.pushButton_3.setStyleSheet("background-color: rgb(52, 156, 161);\n"
"font: 700 9pt \"Arial\";\n"
"\n"
"font: 700 9pt \"Segoe UI\";\n"
"color: black;\n"
"font-size: 11px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_11.raise_()
        self.label_10.raise_()
        self.label_3.raise_()
        self.textEdit.raise_()
        self.label_4.raise_()
        self.textEdit_2.raise_()
        self.label_5.raise_()
        self.textEdit_3.raise_()
        self.pushButton_2.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.pushButton_3.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 761, 571))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("C:/Users/FAAAST 4/Desktop/assets/background-1.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_7.raise_()
        self.tabWidget.raise_()

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Total Products:"))
        self.label_2.setText(_translate("Form", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Category"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Price"))
        self.pushButton.setText(_translate("Form", "Add New Product"))
        self.prev_btn.setText(_translate("Form", "Prev"))
        self.label_8.setText(_translate("Form", "Add Product"))
        self.addNew_btn.setText(_translate("Form", "Add New Product"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.label_3.setText(_translate("Form", " Product Name:"))
        self.label_4.setText(_translate("Form", " Category:"))
        self.label_5.setText(_translate("Form", " Price:"))
        self.pushButton_2.setText(_translate("Form", "Save"))
        self.label_11.setText(_translate("Form", "TextLabel"))
        self.label_12.setText(_translate("Form", "Add Product"))
        self.pushButton_3.setText(_translate("Form", "<"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))