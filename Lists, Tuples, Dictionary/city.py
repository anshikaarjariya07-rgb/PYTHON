#4.	Create a dictionary of n persons where key is name and value is city. 
#a) Display all names
#b) Display all city names
#c) Display student name and city of all students.
#d) Count number of students in each city.
n = int(input("Enter number of persons: "))

students = {}

for i in range(n):
    name = input("Enter name: ")
    city = input("Enter city: ")
    students[name] = city

# a) Display all names
print("\nNames:", list(students.keys()))

# b) Display all cities
print("Cities:", list(students.values()))

# c) Display name and city
print("\nStudent Details:")
for name in students:
    print(name, "-", students[name])

# d) Count students in each city
print("\nNumber of students in each city:")
for city in set(students.values()):
    print(city, ":", list(students.values()).count(city))