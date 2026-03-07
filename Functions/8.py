#8.	Write a program to check whether all the values in a dictionary are same or not using lambda function.
d = {'a':10, 'b':10, 'c':10}

check = lambda x: len(set(x.values())) == 1

print(check(d))