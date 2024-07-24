class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def str(self):
        return f'{self.fname} {self.lname}'
p1 = Person('John', 'Smith')
print(p1.str())