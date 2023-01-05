
import sys
from PyQt5 import QtWidgets, QtCore, uic
import mysql.connector
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from pathlib import Path
import os
from datetime import date
import math

mydb = mysql.connector.connect(
  host="localhost",   # Specify the Host
  user="root",        # Spwcify The user of the Database
  password="123456",  # Specify the password for that user
  database="InstallementManagementSystem"   # Name of Database Created in MySQl Workbench
)
mycursor = mydb.cursor()


# print(mydb)
path = os.path.dirname(__file__)
path = '//'.join(path.split("\\"))
absolutePath = path + "//UI//"


manager_name = ""
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi(absolutePath + "mainwindow.ui", self)
        self.setWindowTitle("Installment management system")
        self.pushButton2.clicked.connect(self.loginfunction)


    def loginfunction(self):
        self.new = LoginWindow()
        self.new.show()
        self.close()

####################################### Login Class ###########################################    
class LoginWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi(absolutePath + "login.ui", self)
        self.setWindowTitle("Log In")
        self.parent = parent
        # self.pushButton.clicked.connect(self.getM_id)
        self.pushButton.clicked.connect(self.on_loginButton)
        self.label_4.hide()
    def getM_name(self):
        un = self.user_name.text()
        print(un)
        global manager_name
        if un =="yameen12":
            manager_name = "Yameen"
        elif un=="mehran22":
            manager_name = "Mehran"
        print(manager_name)
    
       
    def verifyAccount(self):
        un = self.user_name.text()
        pas = self.password.text()
        acc =[]
        check = False
        if self.managerCheck.isChecked():
            try:
                query = "SELECT * FROM manager_accounts"
                mycursor.execute(query)
                acc=mycursor.fetchall()
                print(acc)
            except:
                print("error")
            print(un + pas)
            for x in acc:
                if (un==x[0]) & (pas==x[1]):
                    check = True
                    break
        else:
            try:
                query = 'SELECT * FROM operator_accounts'
                mycursor.execute(query)
                acc=mycursor.fetchall()
                print(acc)
            except:
                print("error")
            print(un + pas)
            for x in acc:
                if (un==x[0]) & (pas==x[1]):
                    check = True
                    break
        # return check
        return True
    def on_loginButton(self):
        if self.managerCheck.isChecked() & self.verifyAccount():
            self.getM_name()
            self.new = ManagerWindow()
            self.new.show()
            self.close()
        elif (self.managerCheck.isChecked()==False) & (self.verifyAccount()):
            # self.getM_id()
            print(self.verifyAccount())
            self.new = OpretorWindow()
            self.new.show()
            self.close()
        else:
            self.label_4.show()
            print("Incorrect Password")
    
####################################### Existing Customer ###########################################

class ExistedCustomer(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi(absolutePath + "ExistedCustomer.ui", self)
        self.setWindowTitle("Existing Customer")
        self.parent = parent
        self.tabWidget.tabBar().setVisible(False)
        self.BuyNewProduct.clicked.connect(self.showTab1)
        self.search.clicked.connect(self.showInfo)
        self.newNext1.clicked.connect(self.showTab2)
        self.newPrev1.clicked.connect(self.showTab0)
        self.newPrev2.clicked.connect(self.showTab1)
        self.newHome1.clicked.connect(self.on_home_btn)
        self.newHome2.clicked.connect(self.on_home_btn)
        self.newHome3.clicked.connect(self.on_home_btn)
        self.Home5.clicked.connect(self.on_home_btn)
        self.newSaveButton.clicked.connect(self.on_safe_btn)
        self.Done.clicked.connect(self.on_home_btn)
    
    def showInfo(self):
        CNIC = self.lineEdit.text()
        try:
            query = f"SELECT CONCAT(Customer.FirstName,' ',Customer.LastName), Customer.PhoneNo, Customer.MonthlyIncome,Customer.FatherName,Customer.MartialStatus, Account.ProductName, Product.Price, Account.Status, CONCAT(Guarantor.FirstName,' ' ,Guarantor.LastName) FROM Customer JOIN Account USING(C_ID) JOIN Product USING(ProductName) JOIN GuarantiedBy USING(C_ID) JOIN Guarantor USING(G_CNIC) WHERE Customer.CNIC = '{CNIC}'"
            mycursor.execute(query)
            data = mycursor.fetchall()
            print(data)
            
        except:
            print("Error")
        self.showTable(data)

    def showTab1(self):
       self.tabWidget.setCurrentIndex(1)
    def showTab0(self):
       self.ExistedInfo.show()
       self.tabWidget.setCurrentIndex(0)
    def showTab2(self):
       self.tabWidget.setCurrentIndex(2)
    def on_home_btn(self):
        self.new = OpretorWindow()
        self.new.show()
        self.close()

    def on_safe_btn(self):
        
        ## Product Information
        PName = self.lineEdit_26.text()
        PDate = self.lineEdit_34.text()
        NetAmount = self.lineEdit_39.text()
        Advance = self.lineEdit_37.text()
        NoOfMonths = int(self.comboBox.currentText())

        ## Calculating Required Figures
        if(NoOfMonths==3):
            AddedAmount = (int(NetAmount)*20)/100
        elif(NoOfMonths==6):
            AddedAmount = (int(NetAmount)*30)/100
        elif(NoOfMonths==9):
            AddedAmount = (int(NetAmount)*40)/100
        elif(NoOfMonths==12):
            AddedAmount = (int(NetAmount)*50)/100

        TotalAmount = int(NetAmount) + math.ceil(AddedAmount)
        Remaining = TotalAmount - int(Advance)
        InstallementPerMonth = math.ceil(Remaining/int(NoOfMonths))
        
        print("Net Amount :",NetAmount)
        print("No Of Months :",NoOfMonths)
        print("Total Amount :",TotalAmount)
        print("Advance :",Advance)
        print("Installement/Month :",InstallementPerMonth)
        print("Remaining :",Remaining)
        
        ## Customer Information
        CNIC = self.lineEdit.text()
        
        ## Account Information
        E_ID = self.lineEdit_24.text()
        CreationDate = PDate
        ExpectedDuration = self.lineEdit_40.text()
        status = "Active"
        InstallementDate = self.lineEdit_68.text()
        
        try:
            ## Fetching Customer ID FROM Database
            query = f"SELECT * FROM Customer WHERE CNIC = '{CNIC}'"
            mycursor.execute(query)
            data = mycursor.fetchall()
            C_ID = data[0][0]
            print("Customer ID: ",C_ID)

            ## Inserting Data In Account Table
            mycursor.execute('''INSERT INTO Account(E_ID,C_ID,ProductName,DateOfCreation,ExpectedDuration,Status) VALUES(%s,%s,%s,%s,%s,%s)
            ''',(E_ID,C_ID,PName,CreationDate,ExpectedDuration,status))
            mydb.commit()
            print("Accounts Added")

            ## Fetching AccountNo From Database
            query = f"SELECT * FROM Account WHERE C_ID = {C_ID} AND DateOfCreation = '{CreationDate}'"
            mycursor.execute(query)
            data = mycursor.fetchall()
            AccountNo = data[0][0]
            print("Account No Fetched : ",AccountNo)


            ## Inserting Data In Payment Table
            mycursor.execute('''INSERT INTO Payment(AccountNo,DateOfPurchased,NetAmount,TotalAmount,Advance,RemainingBalance,MonthlyPayable) VALUES (%s,%s,%s,%s,%s,%s,%s)
            ''',(AccountNo,CreationDate,NetAmount,TotalAmount,Advance,Remaining,InstallementPerMonth))
            mydb.commit()
            print("Payment Added")


            ## Inserting Data In Balance Table
            mycursor.execute('''INSERT INTO Balance(AccountNo,DateofInstallement,AmountRemaining,AmountPaid) VALUES(%s,%s,%s,%s)
            ''',(AccountNo,InstallementDate,Remaining,Advance))
            mydb.commit()
            print("Balance Added")

            ## Inserting Data In InstallementRecord Table
            mycursor.execute('''INSERT INTO InstallementRecord(AccountNo,RemainingInstallements,TotalInstallements) VALUES (%s,%s,%s)
            ''',(AccountNo,NoOfMonths,NoOfMonths))
            mydb.commit()
            print("Installement Record Added")

            ## Fetching Customer ID from Database
            query = f"SELECT * FROM Customer WHERE CNIC = '{CNIC}'"
            mycursor.execute(query)
            data = mycursor.fetchall()
            print(data)
            newC_ID = data[0][0]
            print("C_ID Fetched ",newC_ID)
            ## Fetching AccountNo From Database
            query = f"SELECT * FROM Account WHERE C_ID = {newC_ID} AND DateOfCreation = '{CreationDate}'"
            mycursor.execute(query)
            data = mycursor.fetchall()
            newAccountNo = data[0][0]
            print("Account No Fetched : ",newAccountNo)

            query = f"SELECT Account.AccountNo, CONCAT(Customer.FirstName,' ',Customer.LastName), Payment.MonthlyPayable, Balance.DateofInstallement FROM Account JOIN Customer USING(C_ID) JOIN payment USING(AccountNo) JOIN Balance USING(AccountNo) WHERE AccountNo = {newAccountNo}"
            mycursor.execute(query)
            data = mycursor.fetchall()
            print(data)
            self.label_16.setText(str(data[0][0]))
            self.label_17.setText(str(data[0][1]))
            self.label_30.setText(str(data[0][2]))
            self.label_32.setText(str(data[0][3]))
            self.tabWidget.setCurrentIndex(3)
        except:
            print("error")



    def showTable(self,data):
        if data:
            self.ExistedInfo.insertRow(0)
            for row,form in enumerate(data):
                for column, item in enumerate(form):
                    self.ExistedInfo.setItem(row,column,QTableWidgetItem(str(item)))
                    column+=1
                row_position = self.ExistedInfo.rowCount()
                self.ExistedInfo.insertRow(row_position)



####################################### Opretor Class ###########################################
class OpretorWindow(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__()
        uic.loadUi(absolutePath + "opretorWindow.ui", self)
        self.setWindowTitle("Opretor Window")
        self.parent = parent
        
        self.addNewCustomer.clicked.connect(self.on_customerSelect) 
        self.addInstallment.clicked.connect(self.on_addInstallment)
        self.signOut_btn.clicked.connect(self.on_signout_btn)


    def on_signout_btn(self):
        self.new = LoginWindow()
        self.new.show()
        self.close()
        
    
    def on_customerSelect(self):
        if self.comboCustomer.currentText()=='Existing Customer':
            self.existingCustomer()
        elif self.comboCustomer.currentText()=='New Customer':
            self.newCustomer()
        
        
    def newCustomer(self):
        self.new = ClientFromWindow()
        self.new.show()
        self.close()
    
    def existingCustomer(self):
        self.new = ExistedCustomer()
        self.new.show()
        self.close()
        
    def on_addInstallment(self):
        self.new = AddInstallmentWindow()
        self.new.show()
        self.close()

        
    
####################################### Costomer Class ###########################################

class ClientFromWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi(absolutePath + "clientForm.ui", self)
        self.setWindowTitle("Customer From")
        self.parent = parent
        self.tabWidget.tabBar().setVisible(False)
        self.Next1.clicked.connect(self.showTab1)
        self.Next2.clicked.connect(self.showTab2)
        self.Next3.clicked.connect(self.showTab3)
        self.Prev1.clicked.connect(self.showTab0)
        self.Prev2.clicked.connect(self.showTab1)
        self.Prev3.clicked.connect(self.showTab2)
        self.Home1.clicked.connect(self.on_home_btn)
        self.Home2.clicked.connect(self.on_home_btn)
        self.Home3.clicked.connect(self.on_home_btn)
        self.Home4.clicked.connect(self.on_home_btn)
        self.Home5.clicked.connect(self.on_home_btn)
        self.saveButton.clicked.connect(self.on_save_btn)
        self.Done.clicked.connect(self.on_home_btn)
        
        
    def showTab1(self):
       self.tabWidget.setCurrentIndex(1)
    def showTab0(self):
       self.tabWidget.setCurrentIndex(0)
    def showTab2(self):
       self.tabWidget.setCurrentIndex(2)
    def showTab3(self):
        self.tabWidget.setCurrentIndex(3)
    def showTab4(self):
        self.tabWidget.setCurrentIndex(4)   

    def on_home_btn(self):
        self.new = OpretorWindow()
        self.new.show()
        self.close()
    def on_save_btn(self):
        ## Customer Information
        FirstName = self.lineEdit.text()
        LastName = self.lineEdit_2.text()
        CNIC =  self.lineEdit_3.text()
        FatherName = self.lineEdit_4.text()
        DOB = self.lineEdit_5.text()
        Gender = self.lineEdit_6.text()
        PhoneNo = self.lineEdit_7.text()
        MobileNo =  self.lineEdit_8.text()
        MartialStatus = self.lineEdit_9.text()
        Address = self.lineEdit_10.text()
        WorkPlace = self.lineEdit_11.text()
        Income = self.lineEdit_12.text()
        print("FirstName :"+FirstName)

        ## Guarantor Information
        GFirstName = self.lineEdit_23.text()
        GLastName = self.lineEdit_16.text()
        GCNIC = self.lineEdit_17.text()
        GAddress = self.lineEdit_18.text()
        GPhone = self.lineEdit_19.text()
        GMobile = self.lineEdit_20.text()
        GRelation = self.lineEdit_21.text()
        GWorkPlace = self.lineEdit_22.text()

        ## Product Information
        PName = self.lineEdit_25.text()
        PDate = self.lineEdit_31.text()
        NetAmount = self.lineEdit_27.text()
        Advance = self.lineEdit_28.text()
        NoOfMonths = int(self.comboBox.currentText())
        
        ## Calculating Required Figures
        if(NoOfMonths==3):
            AddedAmount = (int(NetAmount)*20)/100
        elif(NoOfMonths==6):
            AddedAmount = (int(NetAmount)*30)/100
        elif(NoOfMonths==9):
            AddedAmount = (int(NetAmount)*40)/100
        elif(NoOfMonths==12):
            AddedAmount = (int(NetAmount)*50)/100

        ## Fields To be Updated
        
        TotalAmount = int(NetAmount) + math.ceil(AddedAmount)
        Remaining = TotalAmount - int(Advance)
        InstallementPerMonth = math.ceil(Remaining/int(NoOfMonths))
        print("Net Amount :",NetAmount)
        print("No Of Months :",NoOfMonths)
        print("Total Amount :",TotalAmount)
        print("Advance :",Advance)
        print("Installement/Month :",InstallementPerMonth)
        print("Remaining :",Remaining)

        ## Account Information
        E_ID = self.lineEdit_15.text()
        CreationDate = PDate
        ExpectedDuration = self.lineEdit_33.text()
        status = "Active"
        InstallementDate = self.lineEdit_67.text()

        try:
            ## Inserting Data In Customer Table
            print(FirstName,LastName,Address,CNIC,PhoneNo,MobileNo,Income,FatherName,MartialStatus,Gender,DOB,WorkPlace)
            mycursor.execute('''
            INSERT INTO Customer(FirstName,LastName,Address,CNIC,PhoneNo,MobileNo,MonthlyIncome,FatherName,MartialStatus,Gender,DOB,PlaceOfWork) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ''',(FirstName,LastName,Address,CNIC,PhoneNo,MobileNo,Income,FatherName,MartialStatus,Gender,DOB,WorkPlace))
            mydb.commit()

            print("Customer Added")

            ## Inserting Data In Guarantor Table
            mycursor.execute('''
            INSERT INTO Guarantor(G_CNIC,FirstName,LastName,Address,PhoneNo,MobileNo,Relation,PlaceOfWork) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
            ''',(GCNIC,GFirstName,GLastName,GAddress,GPhone,GMobile,GRelation,GWorkPlace))
            mydb.commit()
            print("Guarantor Added")

            ## Fetching Customer ID from Database
            query = f"SELECT * FROM Customer WHERE CNIC = '{CNIC}'"
            mycursor.execute(query)
            data = mycursor.fetchall()
            print(data)
            C_ID = data[0][0]
            print("C_ID Fetched ",C_ID)

            ## Inserting Data In GuarantiedBy Table
            mycursor.execute('''INSERT INTO GuarantiedBy(C_ID,G_CNIC) VALUES(%s,%s)
            ''',(C_ID,GCNIC))
            mydb.commit()
            print("Guarantied By Added")

            ## Inserting Data In Account Table
            mycursor.execute('''INSERT INTO Account(E_ID,C_ID,ProductName,DateOfCreation,ExpectedDuration,Status) VALUES(%s,%s,%s,%s,%s,%s)
            ''',(E_ID,C_ID,PName,CreationDate,ExpectedDuration,status))
            mydb.commit()
            print("Accounts Added")

            ## Fetching AccountNo From Database
            query = f"SELECT * FROM Account WHERE C_ID = {C_ID} AND DateOfCreation = '{CreationDate}'"
            mycursor.execute(query)
            data = mycursor.fetchall()
            AccountNo = data[0][0]
            print("Account No Fetched : ",AccountNo)


            ## Inserting Data In Payment Table
            RemainingNoOfInstallements = int(NoOfMonths)
            mycursor.execute('''INSERT INTO Payment(AccountNo,DateOfPurchased,NetAmount,TotalAmount,Advance,RemainingBalance,MonthlyPayable) VALUES (%s,%s,%s,%s,%s,%s,%s)
            ''',(AccountNo,CreationDate,NetAmount,TotalAmount,Advance,Remaining,InstallementPerMonth))
            mydb.commit()
            print("Payment Added")


            ## Inserting Data In Balance Table
            mycursor.execute('''INSERT INTO Balance(AccountNo,DateofInstallement,AmountRemaining,AmountPaid) VALUES(%s,%s,%s,%s)
            ''',(AccountNo,InstallementDate,Remaining,Advance))
            mydb.commit()
            print("Balance Added")

            ## Inserting Data In InstallementsRecord Table
            mycursor.execute('''INSERT INTO InstallementRecord(AccountNo,RemainingInstallements,TotalInstallements) VALUES (%s,%s,%s)
            ''',(AccountNo,RemainingNoOfInstallements,NoOfMonths))
            mydb.commit()
            print("Installement Record Added")
            
            ## Printing Receipt At The End
            ## Fetching Customer ID from Database
            query = f"SELECT * FROM Customer WHERE CNIC = '{CNIC}'"
            mycursor.execute(query)
            data = mycursor.fetchall()
            print(data)
            newC_ID = data[0][0]
            print("C_ID Fetched ",newC_ID)
            ## Fetching AccountNo From Database
            query = f"SELECT * FROM Account WHERE C_ID = {newC_ID} AND DateOfCreation = '{CreationDate}'"
            mycursor.execute(query)
            data = mycursor.fetchall()
            newAccountNo = data[0][0]
            print("Account No Fetched : ",newAccountNo)

            
            query = f"SELECT Account.AccountNo, CONCAT(Customer.FirstName,' ',Customer.LastName), Payment.MonthlyPayable, Balance.DateofInstallement FROM Account JOIN Customer USING(C_ID) JOIN payment USING(AccountNo) JOIN Balance USING(AccountNo) WHERE AccountNo = {newAccountNo}"
            mycursor.execute(query)
            data = mycursor.fetchall()
            print(data)
            self.label_16.setText(str(data[0][0]))
            self.label_27.setText(str(data[0][1]))
            self.label_29.setText(str(data[0][2]))
            self.label_32.setText(str(data[0][3]))
            self.tabWidget.setCurrentIndex(4)

        except Exception as e:
            print(e)
        
####################################### Installment Class ###########################################
        
class AddInstallmentWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi(absolutePath + "addInstallment.ui", self)
        self.setWindowTitle("Add Installment")
        self.parent = parent
        self.cus_Info.hide()
        self.tabWidget.tabBar().setVisible(False)
        self.Home5.clicked.connect(self.on_home_btn)
        self.Home6.clicked.connect(self.on_home_btn)
        self.search_btn1.clicked.connect(self.showInfo)
        self.addInstallementButton.clicked.connect(self.showTab1)
        self.pushButton_3.clicked.connect(self.on_add_Installement)
        self.newPrev.clicked.connect(self.showTab0)
        
    def showTab1(self):
         self.addInstallementButton.hide()
         self.tabWidget.setCurrentIndex(1)
    def showTab0(self):
         self.addInstallementButton.show()
         self.tabWidget.setCurrentIndex(0)

    def showTable(self,data):
        if data:
            self.tableWidget.insertRow(0)
            for row,form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget.setItem(row,column,QTableWidgetItem(str(item)))
                    column+=1
                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
            self.tableWidget.verticalHeader().setVisible(False)


    def showInfo(self):
        self.cus_Info.show()
        AccountNo = self.lineEdit.text()
        print(" Account No for Existed Customer :",AccountNo)

        try:
            ## Updating Fields 
            print("AccountNO :",AccountNo)
            query = f"SELECT CONCAT(Customer.FirstName,' ', Customer.LastName),Account.ProductName, Payment.TotalAmount, Balance.AmountRemaining, InstallementRecord.RemainingInstallements, InstallementRecord.TotalInstallements, Payment.MonthlyPayable FROM Account JOIN Customer USING (C_ID) JOIN Payment USING(AccountNo) JOIN Product USING(ProductName) JOIN Balance USING(AccountNo) JOIN InstallementRecord USING (AccountNo) WHERE AccountNo = {AccountNo}"
            
            mycursor.execute(query)
            data = mycursor.fetchall()
            print(data)

            TotalInstallements = int(data[0][5])
            paid = (int(data[0][5])) - (int(data[0][4]))
            self.label_10.setText(data[0][0])
            self.label_13.setText(data[0][1])
            self.label_12.setText(str(data[0][2]))
            self.label_14.setText(str(data[0][3]))
            self.label_17.setText(str(data[0][4]))
            self.label_46.setText(str(data[0][6]))
            self.label_15.setText(str(TotalInstallements))
            self.label_18.setText(str(paid))

            query = f"SELECT InstallementNo,ReceivedInstallementDate,InstallementAmount FROM Installement WHERE AccountNo = {AccountNo} "
            mycursor.execute(query)
            data = mycursor.fetchall()
            print(data)
            self.tableWidget.setRowCount(0)
            self.showTable(data)
        except Exception as e:
            print(e)
        
    def on_add_Installement(self):
        AccountNo = self.lineEdit_2.text()
        ReceivedInstallementDate = self.lineEdit_3.text()
        ReceivedAmount = self.lineEdit_4.text()
        try:
            ## Decreasing Remaining Installements by 1
            mycursor.execute(f'''UPDATE InstallementRecord SET RemainingInstallements = RemainingInstallements - 1 WHERE AccountNo = {AccountNo}''')
            mydb.commit()
            print("Remaining Installements Updated")

            ## Fetching Remaining Installements From InstallementRecord 
            query = f"SELECT RemainingInstallements FROM InstallementRecord WHERE AccountNo = {AccountNo}"
            mycursor.execute(query)
            data = mycursor.fetchall()
            remNoOfInst = data[0][0]
            status = "Dead"
            if(remNoOfInst==0):
                ## Updating Account Status in Accounts table
                mycursor.execute(f'''UPDATE Account SET Status ={status} WHERE AccountNo = {AccountNo} ''')
                mydb.commit()
                print("Account Closed i.e Installements Completed")

            ## Fetching No Of Installement No From InstallementRecord Table
            query = f"SELECT TotalInstallements, RemainingInstallements FROM InstallementRecord WHERE AccountNo = {AccountNo}"
            mycursor.execute(query)
            data = mycursor.fetchall()
            IntstallementNo = data[0][0] - data[0][1]

            ## Adding Data to Installements Table
            mycursor.execute('''INSERT INTO Installement(AccountNo,InstallementNo,InstallementAmount,ReceivedInstallementDate) VALUES(%s,%s,%s,%s)
            ''',(AccountNo,IntstallementNo,ReceivedAmount,ReceivedInstallementDate))
            mydb.commit()
            print("Installement Added")

            ## Updating Data to Balance Table
            mycursor.execute(f'''UPDATE Balance SET AmountRemaining = AmountRemaining - {ReceivedAmount}, AmountPaid = AmountPaid + {ReceivedAmount} WHERE AccountNo = {AccountNo}''')
            mydb.commit()
            print("Amount Updated in Balance Table")
    
        except Exception as e:
            print(e)

        self.new = OpretorWindow()
        self.new.show()
        self.close()

    def on_home_btn(self):
        self.new = OpretorWindow()
        self.new.show()
        self.close()
####################################### Manager Class ###########################################
class ManagerWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi(absolutePath + "managerWindow.ui", self)
        self.setWindowTitle("Manager Window")
        self.parent = parent
        self.add_employee_btn.clicked.connect(self.on_addEmployee)
        self.view_employee_btn.clicked.connect(self.on_viewEmployee)
        self.view_customer_btn.clicked.connect(self.on_viewCustomer)
        self.view_record_btn.clicked.connect(self.on_viewRecord)
        self.view_product_btn.clicked.connect(self.on_viewProduct)
        self.signOut_btn.clicked.connect(self.on_signout_btn)
    
    def on_addEmployee(self):
        self.new =NewEmployeeWindow()
        self.new.show()
        self.close()
        
    def on_viewEmployee(self):
        self.new = ViewEmployeeWindow()
        self.new.show()
        self.close()
        
    def on_viewCustomer(self):
        self.new =ViewCustomerWindow()
        self.new.show()
        self.close()
        
    def on_viewRecord(self):
        self.new = ViewRecordWindow()
        self.new.show()
        self.close() 
        
    def on_viewProduct(self):
        self.new = ViewProductWindow()
        self.new.show()
        self.close()
    def on_signout_btn(self):
        self.new = LoginWindow()
        self.new.show()
        self.close()
class NewEmployeeWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi(absolutePath + "addEmployee.ui", self)
        self.setWindowTitle("Add Employee")
        self.parent = parent
        self.prev_btn.clicked.connect(self.on_prev)
        self.add_btn.clicked.connect(self.on_add)
        # self.add_btn.clicked.connect(self.on_prev)

    def mId(self):
        mId =0
        try:
            query = "SELECT M_ID FROM manager WHERE Name = '{}'".format(manager_name)
            mycursor.execute(query)
            mId = mycursor.fetchall()[0][0]
        except Exception as e:
            print(e)
        print(mId)
        return mId

    def on_prev(self):
        self.new = ManagerWindow()
        self.new.show()
        self.close()
    #addind New employee    
    def on_add(self):
        fn = self.first_name.text()
        ln = self.last_name.text()
        cin = self.cnic.text()
        Fn = self.father_name.text()
        dob = self.dob.text()
        gen= self.comboBox.currentText()
        phone = self.phone.text()
        desig= self.comboBox_2.currentText()
        mart= self.comboBox_3.currentText()
        addr = self.address.text()
        work = self.work_hours.text()
        salary = self.salary.text()
        mid = 10
        print(fn,ln,cin,Fn,dob,gen,phone,desig,mart,addr,work,salary,mid)
        try:
            mycursor.execute('''
            INSERT INTO employee(M_ID,FirstName,LastName,CNIC,Salary,WorkHours,Address,DOB,Gender,FatherName,
            Designation,PhoneNo,Martial_status) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ''',(mid,fn,ln,cin,salary,work,addr,dob,gen,Fn,desig,phone,mart))
            mydb.commit()
        except Exception as e:
            print(e)
####################################### View customer Class ###########################################
class ViewCustomerWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi(absolutePath + "viewCustomerWindow.ui", self)
        self.setWindowTitle("Customers Window")
        self.parent = parent
        self.prev_btn.clicked.connect(self.on_prev)
        self.pushButton.clicked.connect(self.on_search)
        self.app_btn.clicked.connect(self.on_app_btn)
        self.showInfo()
        
    def on_prev(self):
        self.new = ManagerWindow()
        self.new.show()
        self.close()


    def on_search(self):
        acc = self.lineEdit.text()
        arg = [acc]
        data = []
        try:
            # q = "SELECT AccountNo,C_ID, concat(FirstName,' ',LastName),ProductName,MobileNo,MonthlyIncome,gender,status,PlaceOfWork FROM account JOIN customer USING(C_ID) WHERE AccountNo = {}".format(acc)
            # mycursor.execute(q)
            # data = mycursor.fetchall()
            mycursor.callproc("show_customer_info",arg)
            for result in mycursor.stored_results():
                data = result.fetchall()
        except Exception as e:
            print(e)
        self.lineEdit.setText("")
        self.tableWidget.setRowCount(0)
        self.showTable(data)
    def showInfo(self):
        total=0
        active = 0
        data = []
        try:
            q = "SELECT COUNT(*) FROM account"
            mycursor.execute(q)
            total = mycursor.fetchall()[0][0]
        except:
            print("error")
        try:
            q = "SELECT COUNT(*) FROM account WHERE status = 'Active'"
            mycursor.execute(q)
            active = mycursor.fetchall()[0][0]
        except:
            print("error")
        dead = total-active
        self.label_6.setText(str(total))
        self.label_7.setText(str(active))
        self.label_8.setText(str(dead))
        try:
            #may be view
            q = "SELECT AccountNo,C_ID, concat(FirstName,' ',LastName),ProductName,MobileNo,MonthlyIncome,gender,status,PlaceOfWork FROM account JOIN customer USING(C_ID)"
            mycursor.execute(q)
            data = mycursor.fetchall()
        except:
            print("error")
        self.showTable(data)

    def on_app_btn(self):
        filt = self.comboBox.currentText()
        data = []
        try:
            q = "SELECT AccountNo,C_ID, concat(FirstName,' ',LastName),ProductName,MobileNo,MonthlyIncome,gender,status,PlaceOfWork FROM account JOIN customer USING(C_ID) WHERE Status = '{}'".format(filt)
            mycursor.execute(q)
            data = mycursor.fetchall()
        except:
            print("error")
        self.tableWidget.setRowCount(0)
        self.showTable(data)
        ##Table show
    def showTable(self,data):
        if data:
            self.tableWidget.insertRow(0)
            for row,form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget.setItem(row,column,QTableWidgetItem(str(item)))
                    column+=1
                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
            
            self.tableWidget.verticalHeader().setVisible(False)
        
####################################### View EmployeeClass ###########################################
class ViewEmployeeWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi(absolutePath + "veiwEmployee.ui", self)
        self.setWindowTitle("Employee Window")
        self.parent = parent
        self.prev_btn.clicked.connect(self.on_prev)
        self.tabWidget.tabBar().setVisible(False)
        self.view_btn.clicked.connect(self.showTab1)
        self.b_btn.clicked.connect(self.showTab0)
        self.search_btn.clicked.connect(self.on_search_btn)
        self.apply_btn.clicked.connect(self.filter)
        self.showDetails()
        self.filter()
        ######### Tab 2 #######
        self.search_btn1.clicked.connect(self.showInfo)
        self.frame.hide()
        # self.apply_btn_2.clicked.connect(self.on_app_btn)
        
    ####################### Tab 1 ##########################
    def showDetails(self):
        total= ""
        recEmp= ""
        oprEmp= ""
        try:
            mycursor.execute(''' SELECT COUNT(*) FROM employee''')
            total=str(mycursor.fetchall()[0][0])
        except:
            print("error")
        try:
            mycursor.execute("SELECT COUNT(*) FROM employee WHERE Designation = 'Recover_Collector'")
            recEmp=str(mycursor.fetchall()[0][0])
        except:
            print("error")
        try:
            mycursor.execute("SELECT COUNT(*) FROM employee WHERE Designation = 'Operator'")
            oprEmp=str(mycursor.fetchall()[0][0])
        except:
            print("error")
        self.label_6.setText(total)
        self.label_7.setText(recEmp)
        self.label_8.setText(oprEmp)

    def showTab1(self):
       self.tabWidget.setCurrentIndex(1)
    def showTab0(self):
       self.tabWidget.setCurrentIndex(0)
    def on_prev(self):
        self.new = ManagerWindow()
        self.new.show()
        self.close()

    #view all Employee
    def showEmployee(self):
        data=[]
        try:
            mycursor.execute(''' SELECT E_ID,M_ID, concat(FirstName,' ',LastName),CNIC,FatherName,PhoneNo, Address,DOB,Gender,Designation,WorkHours,Salary,Martial_status FROM employee''')
            data=mycursor.fetchall()
        except Exception as e:
            print(e)
        self.showTable(data)

    #show tables
    def showTable(self,data):
        if data:
            self.tableWidget.insertRow(0)
            for row,form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget.setItem(row,column,QTableWidgetItem(str(item)))
                    column+=1
                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
            self.tableWidget.verticalHeader().setVisible(False)
    #search employee
    def on_search_btn(self):
        id = self.id_entered.text()
        data=[]
        try:
            query = "SELECT * FROM employee WHERE E_ID='{}'".format(id)
            mycursor.execute(query)
            data=mycursor.fetchall()
        except:
            print("error")
        self.id_entered.setText("")
        self.tableWidget.setRowCount(0)
        self.showTable(data)
    def recoveryEmp(self):
        desig = "Recover_Collector"
        data=[]
        try:
            query = "SELECT E_ID,M_ID, concat(FirstName,' ',LastName),CNIC,FatherName,PhoneNo, Address,DOB,Gender,Designation,WorkHours,Salary,Martial_status FROM employee WHERE Designation='{}'".format(desig)
            mycursor.execute(query)
            data=mycursor.fetchall()
        except:
            print("error")
        
        self.tableWidget.setRowCount(0)
        self.showTable(data)
    def operatorEmp(self):
        desig = "Operator"
        data=[]
        try:
            query = "SELECT * FROM employee WHERE Designation='{}'".format(desig)
            mycursor.execute(query)
            data=mycursor.fetchall()
        except:
            print("error")
        
        self.tableWidget.setRowCount(0)
        self.showTable(data)
        
    def filter(self):
        filt = self.comboBox.currentText()
        print(filt)
        if filt=="Total":
            self.showEmployee()
        elif filt == "Recovery collectors":
            self.recoveryEmp()
        elif filt == "Operators":
            self.operatorEmp()
    ####################### Tab 2 ##########################
    def showInfo(self):
        self.frame.show()
        global e_ID
        c = 0
        e_ID=self.eId_Entered.text()
        try:
            query = "SELECT COUNT(*)FROM account WHERE E_ID = {}".format(e_ID)
            mycursor.execute(query)
            c = mycursor.fetchall()[0][0]
        except:
            print("error")
        self.label_13.setText(str(c))
        arg = [e_ID]
        data = []
        try:
            # query = "SELECT AccountNo, concat(FirstName,' ',LastName) As Name,ProductName, TotalAmount, AmountPaid, MonthlyPayable,ReceivedInstallementDate,AmountRemaining,RemainingInstallements FROM (SELECT * FROM (SELECT * FROM (SELECT * FROM (SELECT * FROM customer c NATURAL JOIN account a WHERE a.E_ID={})c1 Natural JOIN payment)c2 NATURAL JOIN balance) c3 NATURAL JOIN installementrecord) c4 NATURAL JOIN installement".format(e_ID)
            # mycursor.execute(query)
            # data = mycursor.fetchall()
            mycursor.callproc("show_customer_under_emp",arg)
            for result in mycursor.stored_results():
                data = result.fetchall()
        except Exception as e:
           print(e)
        self.eId_Entered.setText("")
        self.tableWidget.setRowCount(0)
        self.showTable2(data)
    def showTable2(self,data):
        if data:
            self.tableWidget_2.insertRow(0)
            for row,form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_2.setItem(row,column,QTableWidgetItem(str(item)))
                    column+=1
                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)
            self.tableWidget_2.verticalHeader().setVisible(False)

        ########### Filter data ###############
    def month(self):
        m = self.comboBox_3.currentText()
        p = {
            "Jan": "01","Feb": "02","Mar": "03","Apr": "04","May": "05","Jun": "06","Jul": "07",
            "Aug": "08","Sep": "09","Oct": "10","Nov": "11","Dec": "12"
            }
        return p.get(m)

    def filt_Rec(self):
        mon = self.month()
        data =[]
        try:
            query = "SELECT AccountNo, concat(FirstName,' ',LastName) As Name,ProductName, TotalAmount, AmountPaid, MonthlyPayable,ReceivedInstallementDate,AmountRemaining,RemainingInstallements FROM (SELECT * FROM (SELECT * FROM (SELECT * FROM (SELECT * FROM customer c NATURAL JOIN account a WHERE a.E_ID={})c1 Natural JOIN payment)c2 NATURAL JOIN balance) c3 NATURAL JOIN installementrecord) c4 NATURAL JOIN installement WHERE ReceivedInstallementDate LIKE '_____{}%'".format(e_ID,mon)


            mycursor.execute(query)
            data = mycursor.fetchall()
        except:
            print("error")
        self.tableWidget.setRowCount(0)
        self.showTable2(data)

    ####### tobe Rec #########
    def filt_tobe_Rec(self):
        mon = self.month()
        data =[]
        try:
            query = "SELECT AccountNo, concat(FirstName,' ',LastName) As Name,ProductName, TotalAmount, AmountPaid, MonthlyPayable,ReceivedInstallementDate,AmountRemaining,RemainingInstallements FROM (SELECT * FROM (SELECT * FROM (SELECT * FROM (SELECT * FROM customer c NATURAL JOIN account a WHERE a.E_ID={})c1 Natural JOIN payment)c2 NATURAL JOIN balance) c3 NATURAL JOIN installementrecord) c4 NATURAL JOIN installement WHERE ReceivedInstallementDate NOT LIKE '_____{}%'".format(e_ID,mon)
            mycursor.execute(query)
            data = mycursor.fetchall()
        except:
            print("error")
        self.tableWidget_2.setRowCount(0)
        self.showTable2(data)

    def on_app_btn(self):
        ch = self.comboBox_2.currentText()
        if ch=="Recovered":
            self.filt_Rec()
        elif ch=="TobeRecovered":
            self.filt_tobe_Rec()
        else:
           self.showInfo()

####################################### Record Class ###########################################
class ViewRecordWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi(absolutePath + "Records.ui", self)
        self.setWindowTitle("Record Window")
        self.parent = parent
        self.prev_btn.clicked.connect(self.on_prev)
        self.pushButton.clicked.connect(self.on_app)
        self.show_record()
        
    
    def month(self):
        m = self.comboBox_3.currentText()
        today = date.today()
        
        if m =="Current":
            return today.month
        else:
            p = {
                "Jan": "01","Feb": "02","Mar": "03","Apr": "04","May": "05","Jun": "06","Jul": "07",
                "Aug": "08","Sep": "09","Oct": "10","Nov": "11","Dec": "12"
                }
            return p.get(m)

    def show_record(self):
        new_acc = 0
        cleared_acc = 0
        acc_rec = 0
        acc_to_rec = 0
        prod_sell = 0
        mon = self.month()

        query = "SELECT count(*) FROM account WHERE DateOfCreation LIKE '_____{}%'".format(mon)
        mycursor.execute(query)
        new_acc= mycursor.fetchall()[0][0]

        query = "SELECT count(*) FROM account WHERE DateOfCreation LIKE '_____{}%' AND Status ='Dead'".format(mon)
        mycursor.execute(query)
        cleared_acc = mycursor.fetchall()[0][0]

        query = "SELECT COUNT(*) FROM installement WHERE ReceivedInstallementDate LIKE '_____{}%'".format(mon)
        mycursor.execute(query)
        acc_rec= mycursor.fetchall()[0][0]

        query = "SELECT COUNT(*) FROM installement WHERE ReceivedInstallementDate NOT LIKE '_____{}%'".format(mon)
        mycursor.execute(query)
        acc_to_rec = mycursor.fetchall()[0][0]

        query = "SELECT COUNT(*) FROM payment WHERE DateOfPurchased LIKE '_____{}%'".format(mon)
        mycursor.execute(query)
        prod_sell= mycursor.fetchall()[0][0]

        self.label_4.setText(str(new_acc))
        self.label_8.setText(str(cleared_acc))
        self.label_11.setText(str(acc_rec))
        self.label_23.setText(str(acc_to_rec))
        self.label_6.setText(str(prod_sell))

    def on_prev(self):
        self.new = ManagerWindow()
        self.new.show()
        self.close()
    def on_app(self):
        self.show_record()
####################################### Product Class ###########################################
class ViewProductWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi(absolutePath + "AddProduct.ui", self)
        self.setWindowTitle("Product Window")
        self.parent = parent
        # self.prev_btn.clicked.connect(self.on_prev)
        self.prev_btn.clicked.connect(self.on_prev)
        self.addNew_btn.clicked.connect(self.showTab1)
        self.pushButton_3.clicked.connect(self.showTab0)
        self.pushButton_2.clicked.connect(self.on_save)
        self.label_10.hide()

        self.showProduct()
        
    
    def on_prev(self):
        self.new = ManagerWindow()
        self.new.show()
        self.close()

    def showTab1(self):
        self.tabWidget.setCurrentIndex(1)

    def showTab0(self):
        self.tabWidget.setCurrentIndex(0)

    def on_save(self):
        pName = self.lineEdit.text()
        category = self.lineEdit_2.text()
        price = self.lineEdit_3.text()
        try:
            mycursor.execute('''
            INSERT INTO product(ProductName,Category,Price) VALUES(%s,%s,%s)
            ''',(pName,category,price))
            mydb.commit()
            print("Product added")
        except:
            print("error")
        self.lineEdit_2.setText("")
        self.lineEdit.setText("")
        self.lineEdit_3.setText("")
        self.label_10.show()
            
    def showProduct(self):
        total = 0
        try:
            mycursor.execute(''' SELECT COUNT(*) FROM product''')
            total=mycursor.fetchall()[0][0]
        except:
            print("error")
        self.label_2.setText(str(total))

        data=[]
        try:
            mycursor.execute(''' SELECT * FROM product''')
            data=mycursor.fetchall()
        except:
            print("error")
        self.showTable(data)

    #show tables
    def showTable(self,data):
        if data:
            self.tableWidget.insertRow(0)
            for row,form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget.setItem(row,column,QTableWidgetItem(str(item)))
                    column+=1
                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
            self.tableWidget.verticalHeader().setVisible(False)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
   # app.setStyleSheet(stylesheet)
    window = MainWindow()
    window.show()
    app.exec_()