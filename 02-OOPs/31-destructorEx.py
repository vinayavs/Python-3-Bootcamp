# DESTRUCTOR - Is responsible for Cleanup activities
# Garbabe Collector - is meant for destroy the obj
# Before going to destroy the object GC calls the destructor to cleanup db and n/w links...

import gc
import time
class Test:
    def __init__(self):  # Constructor
        print('OBJ INITIALIZED')
        print('GC status :',gc.isenabled()) # Enabled by default
    def __del__(self):  # Desctrucor
        print('OBJ DESCTRUCTED')

t = Test()
time.sleep(10)
print('END OF APPLICATION') 
# Alll the objector are eligible for DC at the end of the application, so Destructor executed after 10 secs

# 
# t = Test()
# t = None  # Test() doest have any reference now, so it is elegible for DC, desctructor executed
# time.sleep(10)
# print('END OF THE APPLICATION')


# t1 = Test()
# t2 = Test()
# time.sleep(10)
# print('END OF THE APPLICATION') # 2 TIMES DESTRUCTOR EXECUTED.