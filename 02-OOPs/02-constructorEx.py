class Student:
    '''****STUDENT DETAILS****'''
    def __init__(self):   # CONSTRUCTOR, SPECIAL METHOD
        self.sname = 'vinay'
        self.sno = 100
        self.marks = 98
    def talk(self):
        print('STUDENT NAME :',self.sname)
        print('SUDENT ROLL N0:',self.sno)
        print('STUDENT MARKS:',self.marks)
s = Student()
s.sname
s.sno
s.talk()