class Shape:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color
    def get_area(self):
        print("This method should be implemented by child class")
class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side
    def get_area(self):
        return self.side * self.side
s = Square("orange", 7)
print("Color of square:", s.get_color())
print("Area of square:", s.get_area())
