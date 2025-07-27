# 1. Write a program to accept two numbers from the user and perform division. 
# If any exception occurs, print an error message or else print the result.



try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except:
    print("error")

# 2. Write a program to accept a number from the user and check whether it’s prime or not.
# If user enters anything other than number, handle the exception and print an error message.



try:
    n = int(input("Enter a number: "))
    if n > 1:
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            print("Prime")
        else:
            print("Not Prime")
    else:
        print("Not Prime")
except:
    print("error")

# 3. Write a program to accept the file name to be opened from the user,
# if file exist print the contents of the file in title case
# or else handle the exception and print an error message.



try:
    fname = input("Enter the file name: ")
    f = open(fname, "r")
    print(f.read().title())
    f.close()
except:
    print("error")

# 4. Declare a list with 10 integers and ask the user to enter an index.
# Check whether the number in that index is positive or negative number.
# If any invalid index is entered, handle the exception and print an error message.



nums = [10, -5, 20, -15, 30, 40, -25, 50, -35, 60]
try:
    i = int(input("Enter index (0 to 9): "))
    val = nums[i]
    if val >= 0:
        print("Positive")
    else:
        print("Negative")
except:
    print("error")
