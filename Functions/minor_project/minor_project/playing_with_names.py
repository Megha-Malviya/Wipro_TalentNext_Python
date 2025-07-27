# Project 2
# check if a name is palindrome, count vowels and count frequency of letters

def is_palindrome(name):
    name = name.replace(" ", "")
    if name == name[::-1]:
        print("Yes it is a palindrome.")
    else:
        print("No it is not a palindrome.")

def count_vowels(name):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in name:
        if ch in vowels:
            count += 1
    print("No of vowels:", count)

def letter_frequency(name):
    name = name.replace(" ", "")
    freq = {}
    for ch in name:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    result = []
    for k in sorted(freq):
        result.append(k + "-" + str(freq[k]))
    print("Frequency of letters:", ", ".join(result))

#Input 1
name1 = "bob"
is_palindrome(name1)
count_vowels(name1)
letter_frequency(name1)

print()

#Input 2
name2 = "marcelbentok tanaka"
is_palindrome(name2)
count_vowels(name2)
letter_frequency(name2)
