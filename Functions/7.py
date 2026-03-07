#7.	Write functions to explain mentioned concepts:
#a.	Keyword argument
#b.	Default argument
#c.	Variable length argument
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=20, name="Anshika")
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Anshika")
def total_sum(*numbers):
    total = 0
    for i in numbers:
        total += i
    print("Sum =", total)

total_sum(1,2,3)
total_sum(10,20,30,40)