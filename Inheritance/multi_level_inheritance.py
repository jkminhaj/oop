class Vehicle :
    def __init__ (self , name , price) :
        self.name = name 
        self.price = price 

class Bus(Vehicle):
    def __init__(self,name , price, seat):
        self.seat = seat 
        super().__init__(name,price)

class AcBus(Bus):
    def __init__(self,name,price,seat,temp):
        self.temp = temp
        super().__init__(name,price,seat)
    def __repr__(self):
        return (f"Bus name is : {self.name} , price is {self.price} , temp is {self.temp}")

enaBus = AcBus("Ena",20000,20,16)

print(enaBus)
# print(enaBus.name)
