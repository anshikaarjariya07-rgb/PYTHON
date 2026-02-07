a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

#semi-perimeter
s = (a + b + c) / 2
#area of triangle
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print("Area of the triangle =", area)
