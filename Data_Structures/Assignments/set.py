# 1 - Remove a given item from the set 

s = {10, 20, 30, 40, 50}
print("Original set:", s)
item = int(input("Enter an item to remove: "))

new_set = set()
found = False
for val in s:
    if val != item:
        new_set.add(val)
    else:
        found = True

if found:
    print("Updated set:", new_set)
else:
    print("Item not found, no change:", s)

# 2 - Create an intersection of sets

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print("First set:", s1)
print("Second set:", s2)

intersection_set = set()
for val in s1:
    for val2 in s2:
        if val == val2:
            intersection_set.add(val)

print("Intersection:", intersection_set)

print("----------------------------------------")

# 3 - Create a union of sets

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print("First set:", s1)
print("Second set:", s2)

union_set = set()
for val in s1:
    union_set.add(val)
for val in s2:
    already = False
    for check in union_set:
        if check == val:
            already = True
            break
    if not already:
        union_set.add(val)

print("Union:", union_set)


# 4 - Maximum and Minimum value in a set

s = {25, 10, 45, 5, 30}
print("Set elements:", s)

lst = list(s)
maximum = lst[0]
minimum = lst[0]

for val in lst:
    if val > maximum:
        maximum = val
    if val < minimum:
        minimum = val

print("Maximum value:", maximum)
print("Minimum value:", minimum)
