# Nested Class
# Print name and dob

class Person:
    def __init__(self,name,dd,mm,yyyy):
        print('Person Obj is created...')
        self.name = name
        self.dob = self.Dob(dd,mm,yyyy)
    def info(self):
        print('Name :',self.name)
        self.dob.display()
    class Dob:
        def __init__(self,dd,mm,yyyy):
            print('Dob Obj is created...') 
            self.dd = dd
            self.mm = mm
            self.yyyy = yyyy
        def display(self):
            print('Dob is : {}-{}-{}'.format(self.yyyy,self.mm,self.dd))

p = Person('vin',1,12,1900)
p.info()

     
