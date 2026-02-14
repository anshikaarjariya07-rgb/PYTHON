#4.WAP to enter a string and a substring. 
# You have to print the number of times that the substring occurs in the given string. 
# String traversal will take place from left to right, not from right to left.
# Sample Input
#ABCDCDC
#CDC
#Sample Output
#2
string = input("Enter the string: ")
substring = input("Enter the substring: ")

count = 0
n = len(string)
m = len(substring)

for i in range(n - m + 1):
    if string[i:i+m] == substring:
        count += 1

print("Number of occurrences =", count)