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
      print("Done!")
      connection.commit()
    
   if change == "Name":
      currentname = (input("What is your current Name: "))
      changename = input("What do you want to change your name to?: ")
      testQuery9 = ("UPDATE bankinfo SET Name = %s WHERE Name = %s")
      values = (changename,currentname)
      cursor.execute(testQuery9, values)
      print("Done!")
      connection.commit()
   
   if change == "Type":
      currentname1 = (input("What is your current Name: "))
      changetype = input("What do you want to change your position to?: ")
      testQuery10 = ("UPDATE bankinfo SET Type = %s WHERE Name = %s")
      values = (changetype,currentname1)
      cursor.execute(testQuery10, values)
      print("Done!")
      connection.commit()
     

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
   accountname = input("What is the Name of the account you are trying to close?: ")
   delquery = "DELETE FROM bankinfo WHERE Name = %s"
   values = (accountname,)
   cursor.execute(delquery, values)
   print("Done!")
   connection.commit()


def deposit():
    accountname = input("What is the Name of the account you are trying to add money to?: ")
    money = input("How much money do you want to add?: ")
    testQuery3 = "UPDATE bankinfo SET Money = Money + %s WHERE Name = %s"
    values = (money, accountname)
    cursor.execute(testQuery3, values)
    print("Done!")
    connection.commit()

def withdraw():
    accountname = input("What is the Name of the account you are trying to withdraw money from?: ")
    money = input("How much money do you want to withdraw?: ")
    testQuery3 = "UPDATE bankinfo SET Money = Money - %s WHERE Name = %s"
    values = (money, accountname)
    cursor.execute(testQuery3, values)
    print("Done!")
    connection.commit()

def checkbal():
   pin = int(input("What is your PIN number?: "))
   query = "SELECT Money FROM bankinfo WHERE PIN = %s"
   values = (pin,)
   cursor.execute(query, values)
   resultproduced = cursor.fetchone()
   if resultproduced:
      print("You have",resultproduced[0], "dollars in your account!")
   else:
      "No value"
def signin():

      whattodo = input(("What would you like to do? Enter the numeral of your response: "))
      if whattodo == "1":
         create_new_account()
      elif whattodo == "2":
         modaccount()
      elif whattodo == "3":
         closeaccount()
      elif whattodo == "4":
         deposit()
      elif whattodo == "5":
         withdraw()
      elif whattodo == "6":
         checkbal()
      else:
         print("That is not a valid input")

      



  
print('''
         ____________________________________
         Welcome to the Online Banking System
         Before you begin you must sign in
         ____________________________________
         ''')
name = (input("What is your name?: "))
PIN = int(input("What is your PIN number?: "))
query = "SELECT * FROM bankinfo WHERE PIN = %s AND Name = %s"
values = (PIN,name,)
cursor.execute(query, values) 
if cursor.fetchone():
   print("Sign in Succesful!")
   print('''
      ____________________________________
               Online Banking System

            1. Open an Account
            2. Modify your Account
            3. Close your account
            4. Deposit Money
            5. Withdraw Money
            6. Check Balance
      ____________________________________
      ''')
   while True:
      
      signin()
      response = input("Do you want to perform another transaction? (y/n): ")
      if response.lower() != "y":
         break
else:
   print("Sign in unsuccesful")



cursor.close()

connection.close()