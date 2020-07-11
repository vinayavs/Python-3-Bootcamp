# ADDING INSTANCE VARIABLE TO INSTANCE METHOD
class Test:
    def __init__(self):
        self.a = 10  # Instance variables
        self.b = 30
    def m1(self):    # Instance Method
        self.c = 40  # Instance Variable
        
t = Test()  # a,b will be added to object
t.m1()      # c will be added to object
t.d=50      # d will be added to object, Instace variable added outside of the class
print(t.__dict__) #{'a': 10, 'b': 30, 'c': 40, 'd': 50}

t2 = Test()  # a,b will be added
print(t2.__dict__)  # {'a': 10, 'b': 30}