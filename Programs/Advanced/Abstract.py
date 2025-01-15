#Use the abc module to create an abstract class Shape with an abstract method area(). Implement concrete subclasses Circle and Rectangle.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
circle = Circle(5)
print(circle.area())
rectangle = Rectangle(2, 3)
print(rectangle.area())