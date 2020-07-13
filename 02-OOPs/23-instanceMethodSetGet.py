# INSTANCE METHOD-GETTERS AND SETTERS
class Student:
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setMarks(self, marks):
        self.marks = marks
    def getMarks(self):
        return self.marks
n = int(input('ENTER NO OF STUDENTS :'))
students = []
for i in range(n):
    s = Student()
    name = input('ENTER STUDENT NAME :')
    marks = int(input('ENTER STUDENT MARKS :'))
    s.setName(name)
    s.setMarks(marks)
    students.append(s)
for i in students:
    print('Hello !!',s.getName())
    print('Your Score is :',s.getMarks())
    print()