class Grandparent:
    def gp(self):
        print("Grandparent")

class Parent(Grandparent):
    def parent(self):
        print("Parent")

class Child(Parent):
    def child(self):
        print("Child")

obj = Child()
obj.gp()
obj.parent()
obj.child()