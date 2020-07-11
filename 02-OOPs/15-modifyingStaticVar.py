# If we are trying to modify the static variable by using self or object ref, then the value of the static varible
# won't be changed, Just a new instance variable with that name will be added to that object
class Test:
    a = 10 
    def __init__(self):
        self.b = 20  # Instance variable

t1 = Test()
t2 = Test()
print('t1 :',t1.a,t1.b) # 10 20
print('t1 :',t2.a,t2.b) # 10 20

t1.a = 88  # not possible to modify static variable, it will create new instance variable
t1.b = 99

print('t1 :',t1.a,t1.b) # 88 99
print('t1 :',t2.a,t2.b) # 10 20