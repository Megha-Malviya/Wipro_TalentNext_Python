

#1. Count uppercase and lowercase letters
text = input("Enter a string: ")
upper = 0
lower = 0
for ch in text:
    if 'A' <= ch <= 'Z':
        upper += 1
    elif 'a' <= ch <= 'z':
        lower += 1
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)


#2. Check Palindrome


text = input("Enter a string: ")
rev = ""
for ch in text:
    rev = ch + rev
if text == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


# 3. Repeat first 2 characters n times

text = input("Enter a string: ")
n = len(text)
first2 = text[0] + text[1]
result = ""
for i in range(n):
    result += first2
print(result)


#4. Remove x from first and last

text = input("Enter a string: ")
if len(text) > 0 and text[0] == 'x':
    text = text[1:]
if len(text) > 0 and text[-1] == 'x':
    text = text[:-1]
print(text)



 #5. Repeat last n characters n times

text = input("Enter a string: ")
n = int(input("Enter n: "))
last = text[len(text)-n:]
result = ""
for i in range(n):
    result += last
print(result)

