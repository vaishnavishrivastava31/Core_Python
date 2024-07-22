class Shape:
    def area(self):
        pass


class Circle(Shape):
    def setradius(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14 * self.radius ** 2
        return area
    # def getradius(self):
    #     return self.area


class Rectangle(Shape):
    def setlb(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        area = self.width * self.height
        return area
    # def getlb(self):
    #     return self.area


class Triangle(Shape):
    def setbh(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        area = 0.5 * self.base * self.height
        return area
    # def getbh(self):
    #     return self.area


c = Circle(5)
print(c.area())

r = Rectangle(10, 20)
print(r.area())

t = Triangle(10, 20)
print(t.area())

# from abc import ABC, abstractmethod
# import math
#
#
# class Shape():
#     # @abstractmethod
#     def area(self):
#         pass
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
#
# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#
#     def area(self):
#         return 0.5 * self.base * self.height
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#
# # Example usage:
# circle = Circle(5)
# print(f"Area of circle: {circle.area()}")
#
# triangle = Triangle(10, 5)
# print(f"Area of triangle: {triangle.area()}")
#
# rectangle = Rectangle(4, 6)
# print(f"Area of rectangle: {rectangle.area()}")
