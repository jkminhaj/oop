# Pc model

class PC :
    
    def off (self) :
        print("Shutting down")
        
    def on (self) :
        print("Welcome")
    
    def __init__ (self,ram,hdd,proc) :
        self.ram = ram
        self.hdd = hdd
        self.proc = proc


myPc = PC(8,500,"Core i7")

labPc = PC(16,1000,"Core i9")



print(labPc.ram)
print(myPc.hdd)
print(myPc.proc)
