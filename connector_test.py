import mysql.connector

 

connection = mysql.connector.connect(user = "root", database = "bankproject", password = "RubixCubez13")


 

cursor = connection.cursor()

def modaccount():
   
   change = (input("What would you like to change? Respond with PIN, Name, or Type: "))
   if change == "PIN":
      current = int(input("What is your current PIN number?: "))
      change1 = input("What do you want to change your pin to? Remember it has to be all numbers and 3 digits or less: ")
      testQuery6 = ("UPDATE bankinfo SET PIN = %s WHERE PIN = %s")
      values = (change1,current)
      cursor.execute(testQuery6, values)
      connection.commit()
      testQuery7 = ("SELECT * FROM bankinfo")
      cursor.execute(testQuery7)
      print(cursor.fetchall())
   if change == "Name":
      currentname = (input("What is your current Name: "))
      changename = input("What do you want to change your name to?: ")
      testQuery9 = ("UPDATE bankinfo SET Name = %s WHERE Name = %s")
      values = (changename,currentname)
      cursor.execute(testQuery9, values)
      connection.commit()
      testQuery8 = ("SELECT * FROM bankinfo")
      cursor.execute(testQuery8)
      print(cursor.fetchall())
   if change == "Type":
      currentname1 = (input("What is your current Name: "))
      changetype = input("What do you want to change your position to?: ")
      testQuery10 = ("UPDATE bankinfo SET Type = %s WHERE Name = %s")
      values = (changetype,currentname1)
      cursor.execute(testQuery10, values)
      connection.commit()
      testQuery11 = ("SELECT * FROM bankinfo")
      cursor.execute(testQuery11)
      print(cursor.fetchall())
   else:
      print("That input is not valid")

def create_new_account():
  name = str(input("What is your name?:"))
  type = str(input("Do you want to make a customer account or admin account?: "))
  pin = input("What pin do you want to use? Please make sure to use only numbers, and make sure it is a maximum of 3 digits.: ")
  if type == "customer" and len(pin) < 4 and pin.isnumeric() == True:
     print("Ok, your new account has been added")
     testQuery5 = ("INSERT INTO bankinfo (PIN, Name, Money, Type) VALUES (%s,%s,0,%s)")
     values = (pin,name,type)
     cursor.execute(testQuery5, values)
     connection.commit()
     
  elif type == "admin" and len(pin) < 4 and pin.isnumeric() == True:
     print("Ok, your new account has been added")
     testQuery5 = ("INSERT INTO bankinfo (PIN, Name, Money, Type) VALUES (%s,%s,0,%s)")
     values = (pin,name,type)
     cursor.execute(testQuery5, values)
     connection.commit()
  else:
     print("Something went wrong, try again!")
     
def closeaccount():
   accountpin = int(input("What is the PIN number of the account you are trying to close?: "))
   accountname = list(input("What is the Name of the account you are trying to close?: "))
   accounttype = input("What is the type of account you are trying to close?: ")
   delquery = ("DELETE FROM bankinfo WHERE Name = %i")
   values = (accountname)
   cursor.execute(delquery, values)


#testQuery = ("SELECT * FROM bankinfo")
def deposit():
 
    testQuery3 = ("UPDATE bankinfo SET Name = 'Greg' WHERE Name = 'Bob'")
    cursor.execute(testQuery3)
    connection.commit()
    testQuery4 = ("SELECT * FROM bankinfo")
    cursor.execute(testQuery4)
    print(cursor.fetchall())

    




#create_new_account()
#modaccount()
#closeaccount()
print("Welcome to the online banking system")
action = (input("What would you like to do today - create a new account, modify your account, or close your account (respond with 'create', 'mod', 'close'): "))

if action == "create":
   create_new_account()
if action == 'mod':
   modaccount()
if action == 'close':
   closeaccount()



cursor.close()

connection.close()