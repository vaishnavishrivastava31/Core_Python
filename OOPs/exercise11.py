class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def description(self):
        print(self.model)
        print(self.year)

class ElectricCar(Car):
    def __init__(self, model, year, battery_capacity):
        self.model = model
        self.year = year
        self.battery_capacity = battery_capacity

    def description(self):
        print("Model:", self.model)
        print("Year:", self.year)
        print("Battery capacity:", self.battery_capacity)

e = ElectricCar('Volvo', '2018', '2hrs')
print(e.description())
