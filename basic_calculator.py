# Simple calculator

class Calculator :
    name = "Casio"
    
    def add (self,n1,n2) :
        print(n1+n2)
    
    def deduct (self , n1,n2):
        print(n1-n2)
    
    def prod (self , n1,n2):
        print(n1*n2)
    
    def div (self , n1,n2):
        print(n1/n2)


myCal = Calculator()

myCal.add(2,3)
myCal.deduct(5,3)
myCal.prod(5,3)
myCal.div(5,3)
