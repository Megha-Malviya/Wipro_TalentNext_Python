# 1 - Create a list of 5 integers and access individual elements
lst = [10, 20, 30, 40, 50]
print(lst)
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
print(lst[4])


# 2 -Append a new item to the end of the list (manual)
lst = [1, 2, 3, 4, 5]
new_item = 6
new_lst = [0] * (len(lst) + 1)
i = 0
while i < len(lst):
    new_lst[i] = lst[i]
    i += 1
new_lst[len(lst)] = new_item
lst = new_lst
print(lst)


# 3- Reverse the order of the items in the list (manual)
lst = [1, 2, 3, 4, 5]
rev_lst = [0] * len(lst)
i = 0
while i < len(lst):
    rev_lst[i] = lst[len(lst) - 1 - i]
    i += 1
print(rev_lst)


# 4 - Print the number of occurrences of a specified element (manual)
lst = [1, 2, 3, 2, 4, 2]
x = 2
count = 0
for val in lst:
    if val == x:
        count += 1
print(count)



# 5 - Append items of list1 to list2 in the front (manual)
list1 = [1, 2]
list2 = [3, 4]
combined = [0] * (len(list1) + len(list2))
i = 0
while i < len(list1):
    combined[i] = list1[i]
    i += 1
j = 0
while j < len(list2):
    combined[i + j] = list2[j]
    j += 1
print(combined)


# 6 - Insert a new item before the second element (manual)
lst = [10, 20, 30, 40]
new_item = 15
new_lst = [0] * (len(lst) + 1)
new_lst[0] = lst[0]
new_lst[1] = new_item
i = 1
while i < len(lst):
    new_lst[i + 1] = lst[i]
    i += 1
lst = new_lst
print(lst)



# 7 - Remove the item from a specified index (manual)
lst = [10, 20, 30, 40]
index = 2
new_lst = [0] * (len(lst) - 1)
i = 0
j = 0
while i < len(lst):
    if i != index:
        new_lst[j] = lst[i]
        j += 1
    i += 1
lst = new_lst
print(lst)



# 8 - Remove the first occurrence of a specified element (manual)
lst = [1, 2, 3, 2, 4]
element = 2
new_lst = [0] * (len(lst) - 1)
found = False
i = 0
j = 0
while i < len(lst):
    if lst[i] == element and not found:
        found = True
    else:
        if j < len(new_lst):
            new_lst[j] = lst[i]
            j += 1
    i += 1
if found:
    lst = new_lst
print(lst)
