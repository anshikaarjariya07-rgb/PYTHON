#5.Given a string containing both upper and lower case alphabets. 
# Write a Python program to count the number of occurrences of each alphabet (case insensitive) and display the same
#Sample Input
#ABaBCbGc
#Sample Output
#2A
#3B
#2C 
#1G

string = input("Enter a string: ")

string = string.upper()   

frequency = {}

for char in string:
    if char.isalpha():       
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

for key in sorted(frequency):
    print(frequency[key], key, sep="")