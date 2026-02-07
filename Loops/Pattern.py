n = 5

for i in range(n, 0, -1):

    # Left numbers
    for j in range(1, i + 1):
        print(j, end="")

    # Middle stars
    for j in range(n - i):
        print(" *", end="")

    # Right numbers (skip repeating middle number)
    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()