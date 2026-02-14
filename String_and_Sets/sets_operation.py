#7.	Create 2 sets s1 and s2 of n fruits each by taking input from user and find:
#a)	Fruits which are in both sets s1 and s2
#b)	Fruits only in s1 but not in s2
#c)	Count of all fruits from s1 and s2
n = int(input("Enter number of fruits in each set: "))

s1 = set()
s2 = set()

print("Enter fruits for set s1:")
for i in range(n):
    fruit = input()
    s1.add(fruit.lower())   # lowercase for uniform comparison

print("Enter fruits for set s2:")
for i in range(n):
    fruit = input()
    s2.add(fruit.lower())

# a) Fruits in both sets
common = s1.intersection(s2)

# b) Fruits only in s1
only_s1 = s1.difference(s2)

# c) Count of all fruits from s1 and s2
total_count = len(s1.union(s2))

print("\na) Fruits in both sets:", common)
print("b) Fruits only in s1:", only_s1)
print("c) Total count of distinct fruits:", total_count)