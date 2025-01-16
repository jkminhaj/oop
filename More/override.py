class Person :
    def __init__ (self,name , age) :
        self.name = name 
        self.age = age
    
    def eat (self) :
        print ("Meat , Chicken , Beef")

class DietPerson(Person) :
    def __init__(self,name,age,isOnDiet):
        self.isOnDiet = isOnDiet
        Person.__init__(self,name,age)
    
    def eat(self) :
        print("Only green vegetables")

minhaj = DietPerson("minhaj",20,True);
minhaj.eat() # override : 
