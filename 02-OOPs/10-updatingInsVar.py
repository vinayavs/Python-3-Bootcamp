# UPDATING INSTANCE VARIABLE
class Test():
    def __init__(self):
        self.a = 10
        self.b = 20
t1 = Test()
t1.a = 777  # Updating Instance Variables
t1.b = 888
print('t1 object variables :',t1.a,',',t1.b) # 777 , 888

t2 = Test()
print('t2 object variables :',t2.__dict__) # 10, 20