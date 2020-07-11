# CONSTRUCTOR OVERLOADING IS NOT POSSIBLE
# MOST RECENT CONSTRUCTOR WILL BE TREATED AS THE ONLY ONE CONSTRUCTOR
class Test:
    def __init__(slef):
        print('NO ARG CONSTRUCTOR')
    def __init__(self,x):
        print('ONE ARG CONSTRUCTOR')
# t = Test() #  TypeError: __init__() missing 1 required positional argument: 'x'
t = Test(10) #ONE ARG CONSTRUCTOR