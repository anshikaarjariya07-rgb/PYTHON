#1.	Scan n values in range 0-3 and print the number of times each value has occurred.
# Input number of values
n = int(input("Enter number of values: "))

# Initialize counters
count = [0,0,0,0]   # Index represents the number (0–3)

# Scan values
for i in range(n):
    value = int(input("Enter value (0-3): "))
    
    if 0 <= value <= 3:
        count[value] += 1
    else:
        print("Invalid input! Value must be between 0 and 3.")

# Print results
print("\nOccurrences:")
for i in range(4):
    print(f"{i} occurred {count[i]} times")