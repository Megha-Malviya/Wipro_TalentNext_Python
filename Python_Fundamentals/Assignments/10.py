original = int(input("Enter a number: "))
num = original
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

if original == rev:
    print("It's a palindrome")
else:
    print("Not a palindrome")