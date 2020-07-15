# for every object, a desctructor will be executed seperately.
# while running the application, if want to destroy the list we need to use GC-desctructor.

import time
class Test:
    def __init__(self):
        print('CONSTRUCTOR EXECUTED')
    def __del__(self):
        print('OBJECT DESTROYED')
l = [Test(), Test(), Test()] # list of 3 objects
print('list deleted, 3 objects are elegible for GC now')
del l
time.sleep(10)
print('END OF THE APPLICATION')

# l = [Test(), Test(), Test()] # list of 3 objects
# print('END OF THE APPLICATION')
# print('EOA, All objects are elegible for GC now automatically')