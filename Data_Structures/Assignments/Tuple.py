# 1 - Print the 4th element from first and 4th element from last in a tuple

t = (5, 10, 15, 20, 25, 30, 35)
print("4th element from first:", t[3])
print("4th element from last:", t[len(t) - 4])




# 2 - Check whether an element exists in a tuple or not

t = (1, 2, 3, 4, 5)
x = int(input("Enter element to check: "))
found = False
for val in t:
    if val == x:
        found = True
        break
if found:
    print("Element exists in tuple")
else:
    print("Element not found in tuple")

# 3 - Convert a list into a tuple

lst = [10, 20, 30, 40]
t = ()
for val in lst:
    t = t + (val,)
print("Converted tuple:", t)



# 4 - Find the index of an item in a tuple

t = (10, 20, 30, 40, 50)
x = int(input("Enter element to find index: "))
index = -1
i = 0
for val in t:
    if val == x:
        index = i
        break
    i += 1
if index != -1:
    print("Index of", x, "is", index)
else:
    print("Element not found")





# 5 - Replace last value of tuples in a list to 100 

lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_list = []
for tup in lst:
    values = ()
    for i in range(len(tup)):
        if i == len(tup) - 1:
            values = values + (100,)
        else:
            values = values + (tup[i],)
    new_list.append(values)
print("Updated list:", new_list)
