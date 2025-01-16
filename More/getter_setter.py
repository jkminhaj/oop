class User :
    def __init__ (self , name , age , money) :
        self.name = name 
        self._age = age
        self.__money = money
    
    
    # getter without setter is readonly attribute
    
    @property # this decorator will make the method to attribute
    # using property decorator it's getter now
    def checkAge (self) :
        return self._age ;
    
    
    # getter
    @property    
    def Balance (self) :
        return self.__money ;
        
    
    # @gtterpropertyname.setter : syntex of setter
    
    @Balance.setter
    def Balance(self, value) :
        self.__money = value
    
    
    
    
    

minhaj = User("Minhaj",21,5000)

minhaj.Balance = 500
print(minhaj.Balance)
