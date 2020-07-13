# CLASS METHOD EXAMPLES
# GET NO OF OBJECTES CREATED FOR A CLASS

class Test:
    count = 0 # Static Variable
    def __init__(self):
        Test.count = Test.count + 1  # To access static variable inside constructor
    @classmethod
    def getNoOfObjects(cls):
       print('NO OF OBJS FOR GIVEN CLASS :',cls.count) # Test.count

Test.getNoOfObjects()  # 0
t1 = Test() # Obj Created, Constructor executed automatically
t2 = Test() # Obj Created, Constructor executed automatically
t2 = Test()
t2 = Test()
Test.getNoOfObjects()  # 4

    

