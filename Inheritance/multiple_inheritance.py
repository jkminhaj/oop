class JobHolder :
    def __init__(self,jobTitle) :
        self.jobTitle = jobTitle

class Student :
    def __init__(self,level,id) :
        self.level = level
        self.id = id

class Gender : 
    def __init__ (self , gender):
        self.gender = gender

class Person(JobHolder,Student,Gender) :
    def __init__(self,name,gender,level,id,jobTitle):
        self.name = name 
        JobHolder.__init__(self,jobTitle)
        Student.__init__(self,level,id)
        Gender.__init__(self,gender)
    
    def __repr__ (self):
        return f"Name : {self.name} , Gender {self.gender} , Job : {self.jobTitle} , {self.level} passed"

rahimMia = Person("Rahim Mia" , "Male" , "BSC" , 3545 , "Ricksha wala")

print(rahimMia)
