# ADDING AND ACCESSING STATIC VARIABLES
class Test:
    a = 10 # static variable, within the class but outside of method
    def __init__(self):  # Constructor
        self.x = 20 # Instance variable
        Test.b = 30 # Static Varialbe declared within the constructor
    def m1(self):   # Instance method, because of self
        Test.c = 40 # Static Varialbe declared inside of Instance method
    @classmethod
    def m2(cls):
        Test.d = 50 # static variable declared within class method by using classname.var
        cls.e = 60  # static variable declared by using cls.var
    @staticmethod
    def m3():
        Test.f = 70 # static variable declared at static method
                    
print(Test.__dict__) # To access stactic varialbe, class level so used class name
print(Test.a)        # 10

t = Test()  # Constructor will be executed automaticlly while creating object
print(Test.b) # 30
# print(Test.__dict__)

t.m1()
print(Test.c) # 40

t.m2()
print(Test.d,Test.e) # 50 60 e declared by using cls but for accessing need to use class name only

t.m3()
print(Test.f) # 70

Test.g = 80 # static variable declared outside of the class
print(Test.__dict__) # all the static variables are there in __dict__