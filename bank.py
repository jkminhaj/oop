class Bank :
    name = "UCB"
    
    def __init__ (self,balance) :
        self.balance = balance
        self.min_with = 500
        self.max_with = 50000
    
    def getBalance (self) :
        print(self.balance)
    
    def deposit (self,amount):
        if amount > 0 :
            self.balance += amount
            print(f"{amount} BDT deposit successful")
    
    def withDraw (self,amount):
        if amount >= self.min_with and amount <= self.max_with :
            self.balance -= amount
        else :
            print("Sorry you can't withdraw")

bank1 = Bank(2000)
bank1.withDraw(500)
bank1.deposit(5000)
bank1.getBalance()
