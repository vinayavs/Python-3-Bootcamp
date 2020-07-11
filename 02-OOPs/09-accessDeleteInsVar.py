# ACCESSING AND DELETING INSTANCE VARIABLE
class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
    def display(self):
        del self.a
        print(self.a) # AttributeError: 'Test' object has no attribute 'a'
        print(self.b)
        self.c = 30
        del self.a
t = Test()
t.display()

del t.a
print(t.a) #AttributeError: 'Test' object has no attribute 'a'
del t.b,t.c



# class Test():
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#         self.c = 30
#         self.d = 40
#     def m1(self):
#         del self.d
# t = Test()
# print(t.__dict__) #{'a': 10, 'b': 20, 'c': 30, 'd': 40}

# t.m1()
# print(t.__dict__) # {'a': 10, 'b': 20, 'c': 30}

# del t.b,t.c
# print(t.__dict__) #{'a': 10}

# t2 = Test()
# print(t2.__dict__) # {'a': 10, 'b': 20, 'c': 30, 'd': 40}