# LOCAL VARIABLES
class Test:
    @staticmethod
    def average(list1):
        res = sum(list1)/len(list1)  # res is the local varaible, holding the intermediate results
        print('AVG IS :',res)
    @staticmethod
    def wish(name):
        for i in range(3):  # i is local variable
            print('Hi',name)

l = list(range(10))
Test.average(l)

Test.wish('vinay')

# class Test:
#     def m1(self):
#         a = 10
#         print(a)
#     def m2(self):
#         print(a)
# t = Test()
# t.m1()  # 10
# t.m2()  # NameError: name 'a' is not defined