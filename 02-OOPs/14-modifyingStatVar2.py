class Test:
    a = 10
    def m1(self):
        self.a = 99
t = Test()
t.m1()
print(Test.a) # 10 ClassName.variable => Static Variable
print(t.a) # 99 ObjectRef.var => either static or instance
           # Preference goes to Instance only, If instance var is not available
           # then it will results static variable 

# class Test:
#     a = 10
#     def m1(self):
#         Test.a = 99
# t1 = Test()
# t1.m1()
# print(Test.a) # 99
# print(t1.a) # 99 