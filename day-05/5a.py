with open("in") as f:
    lines = f.read().splitlines()


flag = False
order = []
updates = []
for i in lines:
    if i != '' and not flag:
        order.append(i)
    elif i == '':
        flag = True
    else:
        updates.append(i)

all_updates = []
for i in range(len(updates)):
    update_pages = []
    update_split = updates[i].split(",")
    flag = False
    for j in range(0, len(update_split) - 1):
        if update_split[j]+"|"+update_split[j+1] not in order:
            flag = True
            break
    if not flag:
        all_updates.append(i)
    else:
        all_updates.append(-1)

res = 0
for i in all_updates:
    if i != -1:
        updates_split = updates[i].split(",")
        mid = len(updates_split) // 2
        res += int(updates_split[mid])

print(res)
