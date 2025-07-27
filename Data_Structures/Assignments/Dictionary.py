#Write a program to add a key and value to a dictionary.
d = {0: 10, 1: 20}
d[2] = 30
print(d)



#Write a program to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = {}
for k in dic1:
    result[k] = dic1[k]
for k in dic2:
    result[k] = dic2[k]
for k in dic3:
    result[k] = dic3[k]
print(result)


#Write a program to check if a given key already exists in a dictionary.
d = {1: 100, 2: 200}
k = int(input("Enter key: "))
found = False
for key in d:
    if key == k:
        found = True
        break
if found:
    print("Key exists")
else:
    print("Key does not exist")



#Write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values.
d = {1: "apple", 2: "banana", 3: "cherry"}
print("Keys:")
for key in d:
    print(key)
print("Values:")
for key in d:
    print(d[key])
print("Keys and Values:")
for key in d:
    print(key, d[key])



#Write a program to prepare a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of the keys.
d = {}
for i in range(1, 16):
    d[i] = i * i
print(d)



#Write a program to sum all the values in a dictionary, considering the values will be of int type.
d = {1: 10, 2: 20, 3: 30}
total = 0
for key in d:
    total = total + d[key]
print(total)
