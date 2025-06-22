import math

class Shape:
    """Base class for shapes with polymorphic area method."""
    
    def area(self):
        """Base area method that raises NotImplementedError."""
        raise NotImplementedError("Derived classes need to override this method")


class Rectangle(Shape):
    """Rectangle class that inherits from Shape."""
    
    def __init__(self, length, width):
        """Initialize Rectangle with length and width attributes."""
        self.length = length
        self.width = width
    
    def area(self):
        """Override area method to calculate rectangle's area using formula: length × width."""
        return self.length * self.width


class Circle(Shape):
    """Circle class that inherits from Shape."""
    
    def __init__(self, radius):
        """Initialize Circle with radius attribute."""
        self.radius = radius
    
    def area(self):
        """Override area method to calculate circle's area using formula: π × radius² (use math.pi for π)."""
        return math.pi * (self.radius ** 2)


def main():
    """Main function to demonstrate polymorphism."""
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]
    
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")


if __name__ == "__main__":
    main()