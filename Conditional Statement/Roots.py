import math

# take input from the users
a = float(input("Enter coefficient a:"))
b = float(input("Enter coefficient b:"))
c = float(input("Enter coefficient c:"))

# Calculate the discriminant
D = (b*b - 4 * a * c)

# Checking the roots
if D>0:
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print("The equation has two real and distinct roots.")
    print("Root 1 is: ", root1)
    print("Root 2 is: ", root2)
if D==0:
    root = -b / (2*a)
    print("The equation has real and equal roots.")
    print("Root 1 and 2 are: ",root)
if D<0:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-D) / (2*a)
    print("The equation has imaginary roots.")
    print("Root 1 is : ",real_part,"+ i",imaginary_part)
    print("Root 2 is : ",real_part,"- i",imaginary_part)