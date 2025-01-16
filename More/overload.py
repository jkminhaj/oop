class Person :
    def __init__ (self,name , age) :
        self.name = name 
        self.age = age
    

class DietPerson(Person) :
    def __init__(self,name,age,isOnDiet):
        self.isOnDiet = isOnDiet
        Person.__init__(self,name,age)
    
    # these age called dunder method / magic method we can use substarct , multiply 
    def __add__(self,other):
        return self.age + other.age #self is the first argument , other is 2nd
    
    # mul sign overload
    def __mul__ (self,other) :
        return self.age * other.age
    
    # greater than overload
    def __gt__ (self, other) :
        return self.age > other.age

minhaj = DietPerson("minhaj",20,True);
abid = DietPerson("abid",19,False);

# plus sign overload
print(1+2)
print("2"+"2")
print([2,3,4]+[2,4,5])
print(minhaj+abid)
print(minhaj*abid)
print(minhaj>abid)
print("there is many more dunder method , greater than , less than search for it")

