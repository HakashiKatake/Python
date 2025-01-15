class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing Circle")

class Square(Shape):
    def draw(self):
        print("Drawing Square")

class Triangle(Shape):
    def draw(self):
        print("Drawing Triangle")


circle = Circle()
square = Square()
triangle = Triangle()
print(circle.draw())
print(square.draw())
print(triangle.draw())