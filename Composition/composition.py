# is a  :  Inheritance realtion
# has a  : Composition realtion

class Ram :
    def __init__(self,ram) :
        self.capacity = ram
    

class Hdd :
    def __init__(self, storage) :
        self.capacity = storage


# computer has a ram
class Computer : 
    def __init__(self , ram , storage ) :
        self.Ram = Ram(ram)
        self.Hdd = Hdd(storage) 

pc = Computer(16,200)

print(pc.Ram)
