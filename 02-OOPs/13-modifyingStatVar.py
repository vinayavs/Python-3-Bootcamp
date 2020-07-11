# MODIFYING STATIC VARIABLES
class Test:
    a = 10
    def __init__(self):
        Test.a = 20
    def m1(self):
        Test.a = 30
    @classmethod
    def m2(cls):
        Test.a = 40
        cls.a = 50
    @staticmethod
    def m3():
        Test.a=60

print(Test.a) # 10
t = Test() # Constructor will be executed
print(Test.a) # 20 , So the static variable modified 
t.m1()
print(Test.a)
t.m2()
print(Test.a)
t.m3()
print(Test.a)
Test.a = 70 # modifying static variable outside of the class
print(Test.a)    