#6.	Write a lambda function which gives tuple of max and min from a list.
#Sample input: [10, 6, 8, 90, 12, 56]
#Sample output: (90,6)
nums = [10, 6, 8, 90, 12, 56]

max_min = lambda x: (max(x), min(x))

print(max_min(nums))