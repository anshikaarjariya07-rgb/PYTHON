'''6.Write a program to create a counter to show that how many times the program is executed.'''
file = input("Enter a file: ")

try:
    with open(file, "r") as f:
        count = int(f.read())
except FileNotFoundError:
    print("Error file not found")
    count = 0
except ValueError:
    print("Error: Value error")
    count = 0

count += 1

with open(file, "w") as f:
    f.write(str(count))

print("This program has been executed", count, "times.")