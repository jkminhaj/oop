class Teacher :
    def __init__ (self , name , subject , id) :
        self.name = name
        self.subject = subject
        self.id = id
    def __repr__ (self):
        return(f"Teacher : {self.name} , ID : {self.id} , Subject : {self.subject}")
    
class Student :
    def __init__(self , name , currentClass, id) :
        self.name = name 
        self.id = id
        self.currentClass = currentClass
    
    def __repr__ (self):
        return(f"Student : {self.name} , ID : {self.id} , Class : {self.currentClass}")


class School :
    def __init__ (self , name) :
        self.name = name
        self.teachers = []
        self.students = []
    
    def enroll (self , name , currentClass , fee) :
        if fee < 23000 :
            return f"Please add more {23000-fee} to enroll"
        else :
            id = len(self.students)+1
            student = Student(name , currentClass,id)
            self.students.append(student)
    
    def addTeacher (self , name , subject ) :
        id = len(self.teachers) + 100
        teacher = Teacher(name , subject,id)
        self.teachers.append(teacher)
        
    
    def __repr__ (self) :
        print(f"Welcome to {self.name}"),
        print(".........................")
        
        for teacher in self.teachers :
            print(teacher)
        
        for student in self.students :
            print(student)
        
        return "All done for now"

uu = School("Uttara University")

uu.enroll("Minhaj","BSE",25000)
uu.enroll("Abid","BSE",27000)
uu.enroll("Mahfuz","EEE",27000)
uu.enroll("JEET","IT",200000)

uu.addTeacher("Torikul","DSA")
uu.addTeacher("Siam","EEE")
uu.addTeacher("Mohsin","Programming")

https://www.onlinegdb.com/online_python_compiler#tab-stdin
print(uu)
        
