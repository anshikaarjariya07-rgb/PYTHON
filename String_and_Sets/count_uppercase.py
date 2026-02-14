# 1.Write a program to count and display the number of capital letters in a given string.
string = input("Enter a sentence: ")

count = 0

for char in string:
    if char.isupper():
        count += 1

print("Number of capital letters =", count)