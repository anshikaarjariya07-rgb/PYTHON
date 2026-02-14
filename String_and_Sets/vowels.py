# 2.Count total number of vowels in a given string.
string = input("Enter a sentence: ")

count = 0
vowels = "aeiouAEIOU"

for char in string:
    if char in vowels:
        count += 1

print("Total number of vowels =", count)