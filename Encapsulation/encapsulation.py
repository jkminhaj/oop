class Bank:
    def __init__(self, holder_name, age):
        # Public attribute: Can be accessed directly
        self.holder_name = holder_name
        
        # Protected attribute: Indicated by a single underscore. Meant to be used within the class or subclasses.
        self._age = age
        
        # Private attribute: Indicated by a double underscore. Cannot be accessed directly outside the class.
        self.__balance = 0

    # Public method: Accessible from outside the class
    def deposit(self, amount):
        """Deposit the given amount into the account."""
        if amount > 0:
            self.__balance += amount
            return f"{amount} Taka deposited successfully."
        else:
            return "Invalid deposit amount."

    # Public method: Allows access to the private attribute
    def get_balance(self):
        """Return the current balance."""
        return self.__balance

    # Protected method: Meant for internal or subclass use only
    def _is_adult(self):
        """Check if the account holder is an adult (18 or older)."""
        return self._age >= 18

    # Private method: Used only within this class
    def __log_transaction(self, transaction_type, amount):
        """Log a transaction (private method)."""
        print(f"{transaction_type} of {amount} Taka recorded.")

    # Public method to demonstrate usage of private method
    def withdraw(self, amount):
        """Withdraw the given amount from the account."""
        if amount > self.__balance:
            return "Insufficient balance."
        elif amount <= 0:
            return "Invalid withdrawal amount."
        else:
            self.__balance -= amount
            self.__log_transaction("Withdrawal", amount)  # Using private method inside the class
            return f"{amount} Taka withdrawn successfully."


# Creating an instance of the Bank class
karim = Bank("Karim", 35)

# Accessing public attributes and methods
print(karim.holder_name)          # Output: Karim
print(karim.deposit(50000))       # Output: 50000 Taka deposited successfully.
print(karim.get_balance())        # Output: 50000

# Accessing protected attributes (not recommended, but possible)
print(karim._age)                 # Output: 35

# Accessing private attributes directly (will raise an error)
# print(karim.__balance)          # Uncommenting this line will result in an AttributeError

# Accessing private methods directly (will raise an error)
# karim.__log_transaction("Deposit", 50000)  # Uncommenting this line will result in an AttributeError

# Using public methods that interact with private methods and attributes
print(karim.withdraw(20000))      # Output: 20000 Taka withdrawn successfully.
print(karim.get_balance())        # Output: 30000
