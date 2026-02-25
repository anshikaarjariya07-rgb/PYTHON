#2.	Create a tuple to store n numeric values and find average of all values.
# Input number of values
n = int(input("Enter number of values: "))

values = []

# Take inputs
for i in range(n):
    num = float(input("Enter value: "))
    values.append(num)

# Convert list to tuple
numbers = tuple(values)

# Calculate average
average = sum(numbers) / n

# Display results
print("\nTuple:", numbers)
print("Average:", average)