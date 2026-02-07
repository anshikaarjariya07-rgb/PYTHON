n = int(input("Enter a number: "))
temp = n
digits = len(str(n))
sum = 0

while temp > 0:
    r = temp % 10
    sum += r ** digits
    temp //= 10

if sum == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
