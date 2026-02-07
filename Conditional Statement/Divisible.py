# Taking an input
n = int(input("Enter a number: "))

# Checking the divisibility using if-else condition 
if n % 3 == 0 and n % 5 == 0:
    print("The number is divisible by both 3 and 5")
else:
    print("The number is not divisible by both 3 and 5")
