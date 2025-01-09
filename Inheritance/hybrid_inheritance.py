# Base class
class Animal:
    def __init__(self, species):
        self.species = species

    def show_species(self):
        return f"I am a {self.species}"

# Derived class 1 (Single Inheritance)
class Mammal(Animal):
    def __init__(self, species, is_warm_blooded):
        super().__init__(species)
        self.is_warm_blooded = is_warm_blooded

    def mammal_info(self):
        return f"I am warm-blooded: {self.is_warm_blooded}"

# Derived class 2 (Multiple Inheritance)
class Bird(Animal):
    def __init__(self, species, can_fly):
        super().__init__(species)
        self.can_fly = can_fly

    def bird_info(self):
        return f"I can fly: {self.can_fly}"

# Hybrid class (Combination of Mammal and Bird)
class Bat(Mammal, Bird):
    def __init__(self, species, is_warm_blooded, can_fly):
        Mammal.__init__(self, species, is_warm_blooded)
        Bird.__init__(self, species, can_fly)

    def bat_info(self):
        return f"I am a bat. {self.show_species()}, {self.mammal_info()}, {self.bird_info()}"
    
# Create a Bat instance
bat = Bat("Bat", True, True)

# Display information
print(bat.bat_info())
