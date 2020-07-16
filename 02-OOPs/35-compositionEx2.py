#  HAS-A RELATIONSHIP
class Car:
    def __init__(self,name,model,color):
        self.name = name
        self.model = model
        self.color = color
    def getInfo(self):
        print('Car Name :{}, Model :{}, Color :{}'.format(self.name,self.model,self.color))
class Employee:
    def __init__(self,ename,eno,car):
        self.ename = ename
        self.eno = eno
        self.car = car  # Reference
    def empInfo(self):
        print('Emp Name :',self.ename)
        print('Emp No :',self.eno)
        print('Emp Car Info =>')
        self.car.getInfo()

car = Car('Honda','CRV','Black') # By using car ref, we're creating car obj
emp  = Employee('Vi',1234,car)
emp.empInfo()