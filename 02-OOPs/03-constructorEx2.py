class Test:
    def __init__(self):
        print('CONSTRUCTOR')
    def talk(self,x):
        print('x value is :',x)
t = Test()  # CONSTRUCTOR-will be executed automatically once obj is created
t.talk(10)  # x value is : 10

# class Test():
#     def __init__(self):
#         print('CONSTRUCTOR EXECUTED....')
# t1=Test()
# t2=Test()
