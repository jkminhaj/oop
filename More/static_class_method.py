# Python file explaining static attribute, static method, and class method with examples.

# 1. Static Attribute
# -------------------
# A static attribute is a variable shared across all instances of a class.
# It is defined directly within the class and can be accessed by the class or any instance.

class Example:
    # Static attribute (shared across all instances)
    static_attribute = "Shared by all instances"

    def __init__(self, instance_name):
        self.instance_name = instance_name  # Instance-specific attribute

# Accessing the static attribute
print("Static Attribute (via class):", Example.static_attribute)

# Creating instances
obj1 = Example("Object 1")
obj2 = Example("Object 2")

# Accessing the static attribute via instances
print("Static Attribute (via obj1):", obj1.static_attribute)
print("Static Attribute (via obj2):", obj2.static_attribute)

# Modifying the static attribute via the class
Example.static_attribute = "Updated shared value"
print("Static Attribute after modification (via obj1):", obj1.static_attribute)
print("Static Attribute after modification (via obj2):", obj2.static_attribute)


# 2. Static Method
# -----------------
# A static method is a method that does not require access to the instance (self) or class (cls).
# It is defined using the @staticmethod decorator.
# Useful for utility functions or operations that are independent of class/instance state.

class Utility:
    @staticmethod
    def add_numbers(a, b):
        return a + b

# Accessing a static method
print("Static Method Output:", Utility.add_numbers(5, 7))

# Static methods can also be called via an instance
util = Utility()
print("Static Method Output (via instance):", util.add_numbers(10, 20))


# 3. Class Method
# ----------------
# A class method is a method that operates on the class itself rather than an instance.
# It is defined using the @classmethod decorator and takes 'cls' as its first parameter.
# Useful for factory methods or when you need to modify or access class-level data.

class Factory:
    class_counter = 0  # Static attribute to count instances

    def __init__(self, name):
        self.name = name
        Factory.class_counter += 1  # Increment the counter on every instance creation

    @classmethod
    def get_instance_count(cls):
        return cls.class_counter

# Creating instances
obj1 = Factory("Instance 1")
obj2 = Factory("Instance 2")

# Accessing class method
print("Instance Count (via class method):", Factory.get_instance_count())

# Class methods can also be called via instances
print("Instance Count (via instance):", obj1.get_instance_count())

