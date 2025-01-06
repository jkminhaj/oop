# here constructor == __init__
# constructor is kinda mongoose model for structuring 

class Phone  :
    
    def Flash (self):
        print("Flashlight on")
    
    def Call (self ,num):
        print(f"Calling {num}")
    
    def __init__ (self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price


myPhone = Phone("Minhaj","Samsung",15000)

daddyPhone = Phone("Daddy","Samsung",20000)

mommyPhone = Phone("Mommy","Oppo",18000)

print(myPhone.price)
print(mommyPhone.brand)

myPhone.Call(12245)
