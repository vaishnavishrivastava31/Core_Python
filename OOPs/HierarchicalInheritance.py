class Shape:
    def __init__(self,color,borderwidth):
        self.color=color
        self.borderwidth=borderwidth

class Square(Shape):
    def __init__(self,side,color,borderwidth):
        super(). __init__(color,borderwidth)
        self.side=side
    def area(self):
        return self.side*self.side

class Circle(Shape):
    def __init__(self,radius,color,borderwidth):
        super().__init__(color, borderwidth)
        self.radius=radius
    def area(self):
        return self.radius*self.radius*3.14

s = Square(5,'Black',30)
print(s.side)
print(s.area())
print(s.color)
print(s.borderwidth)

c = Circle(5,'White',30)
print(c.radius)
print(c.area())
print(c.color)
print(c.borderwidth)