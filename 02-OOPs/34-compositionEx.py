# HAS-A RELATION OR COMPOSITION
# Car HAS-A Engine Reference
class Engine:
    def m1(self):
        print('ENGINE FUNCTIONALITIES')
class Car:
    def __init__(self):
        self.engine = Engine()
    def m2(self):
        print('CAR CLASS REQUIRED ENGINE FUNCTIONALITIES')
        self.engine.m1()
t = Car()
t.m2()