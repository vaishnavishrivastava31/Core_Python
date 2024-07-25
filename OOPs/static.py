# class Car:
#     color = "Black"
#
#     @staticmethod
#     def start():
#         print("Starting")
#
#     @staticmethod
#     def stop():
#         print("Stopping")
#
# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name = name

# car1 = ToyotaCar('Fortuner')
# car2 = ToyotaCar('Ford')
# print(car1.color,car1.start(),car1.stop())

class Parent:
    @staticmethod
    def say_hello():
        print("This is a Parent class")

class Child(Parent):

    def say_hello(self):
        print("This is a Child class")
p1 = Parent()
p1.say_hello()
c1 = Child()
c1.say_hello()
