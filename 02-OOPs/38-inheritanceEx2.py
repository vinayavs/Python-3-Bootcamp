# By using super()- we can call parent class members
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eatNDrink(self):
        print('Eating and Drinking...')
class Employee(Person):
    def __init__(self,name,age,eno,esal):
#         self.name = name
#         self.age = age
# Calling Parent Constructor-responsible for Instance var Initialization
        super().__init__(name,age) 
        self.eno = eno
        self.esal = esal
    def work(self):
        print('Programmer')
    def empInfo(self):
        print(self.name)
        print(self.age)
        print(self.eno)
        print(self.esal)

e = Employee('vin',12,12345,10000)
e.eatNDrink()
e.work()
e.empInfo()       