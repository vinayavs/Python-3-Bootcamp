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
# Instace var and static varialbes have same name, so priority will goes to Instance variable 1st
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
