#Create a class to implement method Overriding.
#Same method name, different implementation
#Parent class
class Animal:
    def sound(self):
        print("Animal makes a sound")

#Child class
class Dog(Animal):
    def sound(self):
        print("Dog barks")

#Child class
class Cat(Animal):
    def sound(self):
        print("Cat meows")

a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()   
c.sound()   