class Student:
    schoolName = 'vinlabs'  # static variable , declared at class level
    def __init__(self, sname, sno):  
        self.sname = sname  # Instance variable 
        self.sno = sno
    def getStudentInfo(self):         # Instance Method 
        x = 10              # Local Variable 
        print('STUDENT NAME :',sname) # Instance variable 
    
    @classmethod
    def getSchoolInfo(cls):  # Class Method     
        print('SCHOOL NAME :',cls.schoolName) 
    @staticmethod
    def getSum(a,b): # Static Method, not using self,cls or instance, static class varialbles
        return a+b