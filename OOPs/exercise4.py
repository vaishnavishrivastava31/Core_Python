class Vehicle:
    def __init__(self,  model, year):
        self.model = model
        self.year = year
    def move(self):
        print("Vehicle is moving")
class Car(Vehicle):
    # def __init__(self, model, year):
    #     self.model = model
    #     self.year = year
    def move(self):
        print("Car is moving")
v= Vehicle("Ford", "2021")
print(v.move())
c = Car('ford','2022')
print(c.move())