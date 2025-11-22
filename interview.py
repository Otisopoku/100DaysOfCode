# Base class
class Shape:
    def area(self):
        """
        Base method to calculate area.
        Each subclass should override this method.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def describe(self):
        print("I am a generic shape.")


# Subclass 1
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Polymorphism: overriding the base method
    def area(self):
        return self.width * self.height

    def describe(self):
        print(f"I am a rectangle of width {self.width} and height {self.height}.")


# Subclass 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Polymorphism: overriding the base method
    def area(self):
        return 3.14159 * self.radius ** 2

    def describe(self):
        print(f"I am a circle with radius {self.radius}.")


# Demonstration
shapes = [
    Rectangle(4, 5),
    Circle(3)
]

for shape in shapes:
    shape.describe()  # Polymorphic method call
    print("Area:", shape.area())  # Polymorphic method call
    print("---")
