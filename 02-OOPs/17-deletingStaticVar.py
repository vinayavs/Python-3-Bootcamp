# we can delete static variable by using del classname.var
# also we can use del cls.var for class method
class Test:
    a = 10
    @classmethod
    def m1(cls):
        # del Test.a
        del cls.a
print(Test.__dict__) # Static Variable not yet deleted
Test.m1()  # calling class method classname.method outside of the class
print(Test.__dict__) # Static Variable deleted