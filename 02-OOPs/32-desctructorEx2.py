# DESTRUCTOR EXAMPLE
# t1, t2, t3 ALL ARE POINTING TO SAME OBJECT.
import time
class Test:
    def __init__(self):
        print('CONSTRUCTOR EXECUTED')
    def __del__(self):
        print('*****DESTRUCTOR EXECUTED*****')

t1 = Test()  # Constructor Executed 
t2 = t1
t3 = t2
t4 = Test()  # Constructor Executed
del t1
time.sleep(5)
print('Obj not destroyed after deleting t1')
del t2
time.sleep(5)
print('Obj not destroyed after deleting t2')
time.sleep(5)
print('Removing Last Reference...')
del t3
time.sleep(10)  
# Now Test() is elegible for GC, Obj destroyed after 10 secs controller reaches EOA
# but t4 = Test() still have reference. so after 10sec at EOA - All objs are elegilble for GC, So destructor executed
print('END OF THE APPLICATION')