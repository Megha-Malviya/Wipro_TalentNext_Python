


a = input()
b = input()
c = input()

likes_list = []
temp = ""
for ch in a:
    if ch == "-":
        likes_list.append(temp)
        temp = ""
    else:
        temp = temp + ch
if temp != "":
    likes_list.append(temp)

dislikes_list = []
temp = ""
for ch in b:
    if ch == "-":
        dislikes_list.append(temp)
        temp = ""
    else:
        temp = temp + ch
if temp != "":
    dislikes_list.append(temp)

given_list = []
temp = ""
for ch in c:
    if ch == "-":
        given_list.append(temp)
        temp = ""
    else:
        temp = temp + ch
if temp != "":
    given_list.append(temp)

happiness = 0
for n in given_list:
    found_like = False
    for x in likes_list:
        if n == x:
            happiness = happiness + 1
            found_like = True
            break
    if not found_like:
        for x in dislikes_list:
            if n == x:
                happiness = happiness - 1
                break

print(happiness)
