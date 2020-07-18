# COMPOSITION - STRONG ASSOCIATION BETWEEN CONTAINER AND CONTAINED OBJS
# Ex: Outer Class and Inner Class objects
# Composition and Aggregation have HAS-A Releation
class University:
    def __init__(self):
        self.dept = self.Department()
    class Department:
        pass
u = University()
# d = Department()  # Not possible to create dept obj from outside.

# AGGREGATION - WEAK ASSOCIATION BETWEEN CONTAINER AND CONTAINED OBJS
class Professor:
    pass
class Department:
    def __init__(self,prof):
        self.prof = prof
p = Professor() # without creating dept obj we can create prof obj
csed = Department(p) 
itd = Department(p)