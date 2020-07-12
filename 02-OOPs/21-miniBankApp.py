# MINI BANK APPLICATION
# DIFFERENT TYPES OF VARIABLES IN CLASS 
class Customer:
    '''Author : Vinay
       Purpose: Bank Application'''
    bankName = 'VIN BANK'  # Static Variable, value is fixed for all obj
    def __init__(self, name, balance = 0.0): # Constructor, Instance Variables
        self.name = name
        self.balance = balance
    def deposit(self,amount): #Instance method to access instance variables
        self.balance = self.balance + amount
        print('THE AMOUNT OF {} HAS BEEN CREDITED TO YOUR ACCOUNT & THE BALANCE IS {}'.format(amount,self.balance))
    def withdraw(self,amount):
        if self.balance < amount:
            print('INSUFFICIENT FUNDS TO WITHDRAW')
        else:
            self.balance = self.balance - amount
            print('THE AMOUNT OF {} HAS BEEN DEBITED FROM YOUR ACCOUNT & THE BALANCE IS {}'.format(amount,self.balance))
print('#'*20)
print('WELCOME TO ',Customer.bankName) # Accessing static variable, classname.var
print('#'*20)
name = input('ENTER THE NAME OF THE CUSTOMER :')
c = Customer(name) # Customer object created, So constructor will be executed automatically
while True:
    print('D-DEPOSIT\nW-WITHDRAW\nE-EXIT')
    option = input('PLZ, ENTER YOUR OPTION :')
    if option.lower() == 'd':
        amount = float(input('ENTER AMOUNT TO DEPOSIT :'))
        c.deposit(amount)     #objref.InstanceMethod
    elif option.lower() == 'w':
        amount = float(input('ENTER AMOUNT TO WITHDRAW :'))
        c.withdraw(amount)
    elif option.lower() == 'e':
        print('THANKS FOR CHOOSING',Customer.bankName)
        break
    else:
        print('INVALID OPTION, PLZ CHOOSE ONE OF THE FOLLOWING')