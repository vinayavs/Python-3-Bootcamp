# ACCESSING STATIC VARIABLES
class Test:
    a = 10 # static variable
    def __init__(self):
        print(Test.a)  # to access static variable inside constructor by using self
        print(self.a)  # to access static variable inside constructor by using class name
    def m1(self):
        print(Test.a)  # accessing static variable inside Instance method
        print(self.a)
    @classmethod
    def m2(cls):
        print(cls.a)  # accessing static variable inside class method by using cls
        print(Test.a)
        
    @staticmethod
    def m3():
        print(Test.a) # accessing static variable inside static method

        
t = Test()
print(t.a)    # Accessing static variable outside of the class by using object reference name   
print(Test.a) # Accessing static variable outside of the class by using object class name