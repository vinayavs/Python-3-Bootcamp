class Test():
    def __init__(self):
        print('CONSTRUCTOR EXECUTED')
t = Test()   # CONSTRUCTOR EXECUTED
t.__init__() # CONSTRUCTOR EXECUTED, calling constructor explicitly, new object wont be created