class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
        # area = width * length
    def get_width(self):
        return self.width
    def get_length(self):
        return self.length
    def area(self):
        return self.width * self.length
    def get_area(self):
        return self.area()
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        # area = 3.14 * radius * radius
    def get_radius(self):
        return self.radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def get_area(self):
        return self.area()
r = Rectangle(5, 5)
print(r.get_width())
print(r.get_length())
print(r.get_area())
c = Circle(5)
print(c.get_radius())
print(c.get_area())