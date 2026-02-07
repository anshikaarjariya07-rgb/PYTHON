n = int(input("Enter the value of n: "))
sum = 0.0

for i in range(1, n + 1):
    sum = sum + (1 / i)

print("Sum of the series is:", sum)