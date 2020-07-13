# ACCESSING MEMBERS OF ONE CLASS FROM ANOTHER CLASS
class Employee:
    def __init__(self,name,sal): # Constructor
        self.name = name
        self.sal = sal
    def display(self): #Instance Method
        print('EMP NAME :',self.name)
        print('EMP SAL :',self.sal)
class Manager:
    def updateSal(emp): # Static method
        emp.sal = emp.sal+10000
        emp.display()

emp = Employee('vin',25000)
Manager.updateSal(emp)