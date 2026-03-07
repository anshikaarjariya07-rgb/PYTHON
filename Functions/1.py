#1.Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
#(Note: Do not use built-in functions.)
def find_max_min(numbers):
    max_num = numbers[0]
    min_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    return max_num, min_num

nums = [10, 6, 8, 90, 12, 56]
print(find_max_min(nums))