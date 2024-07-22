# class Person:
#     name = "vaishnavi"
# p = Person()
# print(p.name)

# class Car:
#     color = 'black'
#     brand = 'Ford'
#     model = 'Mustang'
#     year = '2021'
#     price = '800000'
# c = Car()
# print(c.color)
# print(c.brand)
# print(c.model)
# print(c.year)
# print(c.price)

# class Student:
#     name = 'riya'
#     def __init__(self):
#         print(self)      # It represent student object
#         print('Hello World')
# s1 = Student()
# print(s1.name)
# print(s1)

# class Student:
#     def __init__(self, fname, lname, classroom):
#         self.fname = fname
#         self.lname = lname
#         self.classroom = classroom
# s1 = Student('vaishnavi','shrivastava','12th')
# print(s1.fname)
# print(s1.lname)
# print(s1.classroom)

# class Student:
#     def __init__(self):
#         pass
#
#     def __init__(self,fname,lname,classroom):
#         self.fname=fname
#         self.lname=lname
#         self.classroom = classroom

# s = Student()
# print(s.fname)
# print(s.lname)
# print(s.classroom)
# print(s)

# class Student:
#     def setfname(self, fname):
#         self.fname = fname
#
#     def getfname(self):
#         return self.fname
#
#
# s = Student()
# s.setfname('vaishnavi')
# print(s.getfname())

# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#     def printname(self):
#         print(self.fname, self.lname)
# p = Person('John', 'Smith')
# p.printname()

# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#     def printname(self):
#         print(self.fname, self.lname)
# p = Person('John', 'Smith')
# class Student(Person):
#     pass
# x = Student("Vaishnavi","Shrivastava")
# x.printname()
# p.printname()

# print("Polymorphism with Class methods:\n")
# class India:
#     def capital(self):
#         print("New Delhi is the capital of India")
#     def languages(self):
#         print("Hindi is the primary language of India")
#     def type(self):
#         print("India is a developing country")
# class USA:
#     def capital(self):
#         print("Washington is the capital of USA")
#     def languages(self):
#         print("English is the primary language of USA")
#     def type(self):
#         print("USA is a developing country")
# ind = India()
# usa = USA()
# for country in(ind,usa):
#     country.capital()
#     country.languages()

# class fruits:
#     def __init__(self):
#         self.price = 100
#         self.bags = 5
#     def display(self):
#         print(self.bags)
# obj = fruits()
# obj.display()

