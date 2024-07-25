class GrandParent:
    def GP(self):
        print("Parent class is GrandParent")
class Parent(GrandParent):
    def parent(self):
        print("Parent class is Parent")

class Child(Parent):
    def child(self):
        print("Child class is Child")

c= Child()
c.child()
c.GP()
c.parent()