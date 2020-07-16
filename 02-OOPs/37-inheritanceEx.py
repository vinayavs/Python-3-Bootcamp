# ACCESSNG PARENT MEMBERS FROM CHILD
# IS-A RELATIONSHIP OR INHERITANCE
class Parent:
    a = 10
    def __init__(self):
        print('Parent Constructor')
        self.b = 20  
    def m1(self):
        print('Parent Instance Method')
    @classmethod
    def m2(cls):
        print('Parent Class Method')
    @staticmethod
    def m3():
        print('Parent Static Method')
class Child(Parent): # Inheriting Parent Class
    pass

c = Child() # No Constructor,So Parent Constructor will be inherited
print(c.a) # 10, Parent Class Static Variable
print(c.b) # 20, Parent Class Instance Variable 
c.m1()  # Parent Instance Method
c.m2()  # Parent Class Method
c.m3()  # Parent Static Method