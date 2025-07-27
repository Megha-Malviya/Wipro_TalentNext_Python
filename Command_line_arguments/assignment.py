import sys

# Program 1: Sum of first two numbers from command line arguments 
if len(sys.argv) < 3:
    print("Give at least two numbers")
    sys.exit()

def text_to_num(text):
    num = 0
    for ch in text:
        if ch == '0': d = 0
        elif ch == '1': d = 1
        elif ch == '2': d = 2
        elif ch == '3': d = 3
        elif ch == '4': d = 4
        elif ch == '5': d = 5
        elif ch == '6': d = 6
        elif ch == '7': d = 7
        elif ch == '8': d = 8
        elif ch == '9': d = 9
        num = num * 10 + d
    return num

n1 = text_to_num(sys.argv[1])
n2 = text_to_num(sys.argv[2])
print("Sum of two numbers:", n1 + n2)


# Program 2: Show file name and welcome message
if len(sys.argv) > 3:
    print("File name:", sys.argv[0])
    print("Welcome message:", sys.argv[3])
else:
    print("No welcome message given")


#  Program 3: Sum of prime numbers from next 10 arguments 
if len(sys.argv) >= 14:
    numbers = [text_to_num(sys.argv[i]) for i in range(4, 14)]
    total = 0
    for n in numbers:
        if n > 1:
            prime = True
            d = 2
            while d < n:
                if n % d == 0:
                    prime = False
                    break
                d += 1
            if prime:
                total += n
    print("10 numbers:", numbers)
    print("Sum of prime numbers:", total)
else:
    print("Not enough numbers for prime sum")





#sample input:

#run in command line as: python assignment.py 5 7 Hello 2 3 4 5 6 7 8 9 10 11 13
#output is:
"""
Sum of two numbers: 12
File name: assignment.py
Welcome message: Hello
10 numbers: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
Sum of prime numbers: 28"""