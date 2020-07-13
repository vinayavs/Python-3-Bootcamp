# INSTACNCE METHOD ALWAYA TALKING ABOUT A PARTICULAR OBJECT
# Methods having instance variable are called as Instance Methods
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self): # Instance Method 
        print('Hello,',self.name)
        print('You have scored :',self.marks)
    def grade(self): # Instance Method
        if self.marks >= 60:
            print(self.name,'=> A GRADE')
        elif self.marks >= 35:
            print(self.name,'=> B GRADE')
        else:
            print(self.name,'=> FAILED')
s = Student('vinay',98)
s.display()
s.grade()