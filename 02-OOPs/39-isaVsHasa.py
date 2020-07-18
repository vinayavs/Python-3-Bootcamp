# IS-A VS HAS-A
# IS-A - GO WITH INHERITANCE=> EXISTING FUNCTIONALITY + NEW (EXTENDIBILITY)
#  HAS-A- GO WITH COMPOSITION => IF WE WANT TO USE EXISTING FUNTIONALITY ONLY

class Car:
    def __init__(self,name,model,color):
        self.name = name
        self.model = model
        self.color = color
    def getInfo(self):
        print('\tCar Name :{}\n\tModel :{}\n\tColor :{}'.format(self.name,self.model,self.color))
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eatNdrink(self):
        print('Eating and Dringking...')
class Employee(Person):
    def __init__(self,name,age,eno,esal,car):
        super().__init__(name,age)
        self.esal = esal
        self.eno = eno
        self.car = car  # Reference
    def work(self):
        print('Programmer...')
    def empInfo(self):
        print('Emp Name :',self.name)
        print('Emp Age :',self.age)
        print('Emp No :',self.eno)
        print('Emp Sal :',self.esal)
        print('Emp Car Info =>')
        self.car.getInfo()  # Using Car functionality because we have reference 
        
car = Car('Honda','CRV','Black')
emp = Employee('Vin',21,1234,10000,car)
emp.eatNdrink() # Inherited
emp.work()
emp.empInfo()
