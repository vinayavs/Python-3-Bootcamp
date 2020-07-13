# CLASS METHOD
class Birds:
    wings = 2  # Fixed for all objs, static variable(class level)
    @classmethod
    def fly(cls,name):
        print('{} flying with {} wings!!'.format(name, cls.wings))
Birds.fly('owl') # No need to create object, Cuz of we dont have any instance variables
