# TYPES OF INHERITANCE
# SINGLE INHERITANCE 
# 1 TO 1  , One Parent to One Child
class P:
    def m1(self):   
        print('Parent Method...')
class C(P):   # Java - Class C extends P{}
    def m2(self):
        print('Child Method...')
c = C()
c.m1()  # Parent Method...
c.m2()  # Child Method...
    
# MULTI-LEVEL INHRITANCE - Multiple levels of Inheritance
# Multiple Classes to single class but one after another
# Grand P - P - C
class P:
    def m1(self):
        print('Parent Method')
class C(P):
    def m2(self):
        print('Child Method')
class SubC(C):
    def m3(self):
        print('Sub Child Method')

subc= SubC()
subc.m1()
subc.m2()
subc.m3()

# HIERARCHICAL INHERITANCE
# ONE CLASS TO SAME LEVEL MULTIPLE CLASSES
class P:
    def m1(self):
        print('Parent Method...')
class C1(P):
    def m2(self):
        print('1st Child Method...')
class C2(P):
    def m3(self):
        print('2nd Child Method..')
c1 = C1()
c1.m1()
c1.m2()
# c1.m3() # AttributeError: 'C1' object has no attribute 'm3'
c2 = C2()
c2.m1()
c2.m3()
# c2.m2() #AttributeError: 'C2' object has no attribute 'm2'

# MULTIPLE INHERITANCE
# Multiple Class to Single Class
# Order of Parent Class is important to achilve diamond access/ambiguity problem
class P1:
    def m1(self):
        print('Parent-1 Method-1')
class P2:
    def m1(self):
        print('Parent-2 Method-1')
    def m2(self):
        print('Parent-2 Method')
class C(P1,P2):  # Parent-1 Method-1, C(P2,P1)=> Parent-2 Method-1
    def m3(self):
        print('Child Method')
c = C()
c.m1()
c.m2()
c.m3()

# HYBRID INHERITANCE 
# COMBINATION OF SINGLE, MULTI-LEVEL, MULTIPLE, HIERARCHICAL
# MRO - METHOD RESOLUTION ORDER
# PYTHON WONT SUPPORT CYCLIC INHERITANCE
# class A(A):  # Cyclic Inheritance
#     pass
# # Cyclic Inheritance
# class A(B):
#     pass
# class B(A):
#     Pass