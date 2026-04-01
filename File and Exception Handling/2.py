#2.	Store integers in a file.
#a.	Find the max number
#b.	Find average of all numbers
#c.	Count number of numbers greater than 100
f = open("number.txt", "w")
f.write("120\n130\n20\n300\n20")
f.close()
f = open("number.txt", "r")
numbers = []
for line in f:
    numbers.append(int(line))
print(numbers)
f.close()
print("The maximum number is : ", max(numbers))
avg = sum(numbers)/len(numbers)
print("The average of numbers is: ", avg)
count = 0
for n in numbers:
    if n > 100:
        count += 1
print("Numbers greater than 100:", count)