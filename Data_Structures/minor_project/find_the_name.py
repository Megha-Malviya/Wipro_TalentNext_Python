#Given a string of words, find how many times the name Alex appears in that string. 
# For example, in Hi Alex WelcomeAlex Bye Alex the name Alex appears 3 times.

text = "Hi Alex WelcomeAlex Bye Alex"
name = "Alex"
count = 0
length = len(text)
name_length = len(name)

i = 0
while i <= length - name_length:
    match = True
    for j in range(name_length):
        if text[i + j] != name[j]:
            match = False
            break
    if match:
        count = count + 1
    i = i + 1

print(count)
