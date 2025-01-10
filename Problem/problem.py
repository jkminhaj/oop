# Create a Product class and a Shop class.
# Inside the Shop class, create a method name add_product which adds products using the Product class to the Shop class.
# Inside the Shop class, create a method name buy_product which is used to buy a product and check whether this product is available or not. If you successfully buy a product, then throw a Congress message.

class Product :
    def __init__ (self , name , price) :
        self.name = name 
        self.price = price

class Shop() :
    def __init__ (self,name) :
        self.name= name
        self.products=[]
    
    def add_product (self,name,price) :
        # Product.__init__(self , name,price)
        product = Product(name,price)
        self.products.append(product)
    
    def buy_product(self,name,amount) :
        
        for i, item in enumerate(self.products) :
            if name == item.name:
                self.products.pop(i)
                return print("item purchase successful")
            else :
                return print("Stock out !")
    
    def getItems(self):
        print("_____Item List _________")
        for item in self.products:
            print("    ",item.name)
        print("_____        _________")
shopno = Shop("Shopno")
shopno.add_product("Egg",20)
shopno.add_product("Salt",40)
shopno.add_product("Rice",60)
shopno.add_product("Rice",60)

shopno.buy_product("Egg",35)
shopno.buy_product("Egg",50)
shopno.getItems()

                
    
    
        
