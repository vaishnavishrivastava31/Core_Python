class A:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}")


class B:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"The dance is {self.dance}")


class C(A, B):
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name


o = C("Kathak", "Shivani")
print(o.name)
print(o.dance)
o.show()