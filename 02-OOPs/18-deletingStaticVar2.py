# we can’t modify/delete static variable by using obj ref or self. But we can access 
# static variables by using obj ref, self and class
class Test:
    a = 10
    def __init__(self): # Constructor 
        Test.b = 20
        del Test.a
    def m1(self): # Static Mehtod
        Test.c = 30
        del Test.b
    @classmethod
    def m2(cls):
        cls.d = 40
        del Test.c
    @staticmethod
    def m3():
        Test.e = 50
        del Test.d
        
print(Test.__dict__)  # a = 10

t = Test()  # obj created, Constructor executed automatically
print(Test.__dict__)  # b = 20

t.m1() # Calling Instance Method
print(Test.__dict__)  # c = 30

Test.m2() # Calling Class Method, we can also call by using obj ref
print(Test.__dict__) # d = 40

Test.m3() # Calling Static Method, we can also call by using obj ref
print(Test.__dict__) # e = 50