# function inside the class is called method

# pass self keyword in all methods as default in python only
# if the parameter is empty then will show error

class Phone :
    # These are attributes
    name = "Samsung"
    ram = 8
    color = "blue"
    
    def ring(self) :
        print("phone is ringing")
        # use return or pass 
    
    def sendSMS(self , num , text):
        print(f"{text} from  :{num}")

# calling new : use parenthesis to make new

myPhone = Phone()

print(myPhone.name)
myPhone.ring()

myPhone.sendSMS(1314747,"hi")
