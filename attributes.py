# Class attributes

class Shop :
    cart = [] # class attribute
    
    def __init__ (self , buyer) :
        self.buyer = buyer
    
    def addToCart (self,item) :
        self.cart.append(item)
    
newbuyer = Shop("minhaj")
newbuyer.addToCart("Mobile")

oldbuyer = Shop("Abid")
oldbuyer.addToCart("PC")

print(newbuyer.cart)
print(oldbuyer.cart)

# class attributes work globally

# instance attributes

class NewShop :
    name = "Jamjam"
    
    def __init__ (self,buyer):
        self.buyer = buyer
        self.cart = [] # instance attribute
    
    def addToCart (self,item):
        self.cart.append(item)


rahim = NewShop("Rahim")

karim = NewShop("Karim")

rahim.addToCart("Suger")
rahim.addToCart("Salt")

karim.addToCart("Lego Set")
karim.addToCart("Toy Gum")

print(karim.cart)
print(rahim.cart)
        
