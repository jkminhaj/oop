class Gadget : 
    def __init__ (self,name ,brand,price) :
        self.name = name 
        self.brand = brand 
        self.price = price 


class Phone(Gadget) : 
    def __init__(self,name,brand,price,ram,memory) :
        self.ram = ram 
        self.memory = memory
        super().__init__(name,brand,price)

myPhone = Phone("A20","Samsung",20000,64,250)

print(myPhone.price)
        
