class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
    def description(self):
        print(self.model)
        print(self.year)
c = Car('Mustang', '2023')
c.description()