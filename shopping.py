class Shop :
    
    def __init__ (self , name) :
        self.name = name
        self.cart = []
    
    def addToCart (self , item , quantity , price) :
        product = {"item":item,"quantity":quantity,"price":price}
        self.cart.append(product)
        
    def removeItem (self , item):
        loc = False
        
        for index , i in enumerate(self.cart) :
            if item == i["item"]:
                loc = index
        
        del self.cart[loc]
    
    def checkout (self,amount) :
        total = 0 
        
        for item in self.cart :
            total += item["quantity"] * item["price"]
            
        if amount >= total :
            print(f"here is your change {amount-total}")
        
        else : 
            print(f"please provide {total-amount} more")
        
        


minhaj = Shop("minhaj")

minhaj.addToCart("Rice",2,70)
minhaj.addToCart("Potato",5,30)
minhaj.addToCart("Salt",1,20)
minhaj.addToCart("Sugar",1,100)

minhaj.removeItem("Rice")
print(minhaj.cart)
