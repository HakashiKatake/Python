
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

rectangle = Rectangle(2, 3)
print(rectangle.area()) 