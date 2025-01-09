from abc import ABC, abstractmethod

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass  # Subclasses must implement this method

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass  # Subclasses must implement this method


# Concrete Class 1
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Concrete Class 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.1416 * self.radius


# Example Usage
shapes = [
    Rectangle(5, 3),
    Circle(7)
]

for shape in shapes:
    print(f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")
