n = int(input("Enter a number: "))
rev = int(str(n)[::-1])

if n == rev:
    print("Palindrome number")
else:
    print("Not a palindrome number")
