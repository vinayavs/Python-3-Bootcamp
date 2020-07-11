class Test:
    a = 10 
    def __init__(self):
        self.b = 20  # Instance variable

t1 = Test()
t2 = Test()
print('t1 :',t1.a,t1.b) # 10 20
print('t1 :',t2.a,t2.b) # 10 20

Test.a = 88  # static variable will be modified by using classname.var
Test.b = 99  # adding/new static variable, no impact on instance variable self.b
# Instance var and static varialbles have same name, so priority will goes to Instance variable 1st
# if install variable is not available then static variable will be available
print('t1 :',t1.a,t1.b) # 88 20  
print('t1 :',t2.a,t2.b) # 88 20
print('Test :',Test.a,Test.b) # 88,99

# 
# class Test:
#     a = 10
#     def __init__(self):
#         self.b = 20
# t1 = Test()
# t2 = Test()
# Test.a = 88
# t1.b = 99
# print('t1 :',t1.a,t1.b) #88 99
# print('t2 :',t2.a,t2.b) #88 20



# class Test:
#     a = 10
#     def __init__(self):
#         self.b = 20
#     def m1(self):
#         self.a = 88
#         self.b = 99
#     @classmethod
#     def m2(cls):
#         cls.a = 66
#         cls.b = 77
        
# t1 = Test()
# t2 = Test()
# t1.m1()
# print('t1 :',t1.a,t1.b) # 88 99
# print('t2 :',t2.a,t2.b) # 10 20

# t2.m1()
# print('t1 :',t1.a,t1.b) # 88 99
# print('t2 :',t2.a,t2.b) # 88 99

# class Test:
#     a = 10
#     def __init__(self):
#         self.b = 20
#     @classmethod
#     def m1(cls):
#         cls.a = 66
#         cls.b = 77
# t1 = Test()
# t2 = Test()
# t1.m1()  # calling classmethod with obj ref, but recommended to use classname
# print('t1 :',t1.a,t1.b) # 66 20
# print('t2 :',t2.a,t2.b) # 66 20
# print('Test :',Test.a,Test.b) # 66 77


