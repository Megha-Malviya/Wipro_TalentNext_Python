
# 1. Write a function to return the sum of all numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20


def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(sum_of_list([8, 2, 3, 0, 7]))

# 2. Write a function to return the reverse of a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def reverse_string(text):
    return text[::-1]
print(reverse_string("1234abcd"))

# 3. Write a function to calculate and return the factorial of a number (a non-negative integer).

def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result
print(factorial(5))


# 4. Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.

def count_upper_lower(text):
    upper_count = 0
    lower_count = 0
    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    print("upper", upper_count)
    print("lower", lower_count)
count_upper_lower("HelloWorld")

# 5. Write a function to print the even numbers from a given list. 
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

def print_even_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(num, end=" ")
print_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
print()

# 6. Write a function that takes a number as a parameter and checks whether the number is prime or not.
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
print(is_prime(7))

