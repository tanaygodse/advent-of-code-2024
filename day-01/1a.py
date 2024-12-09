with open("in") as f:
    lines = f.read().splitlines()
items_a = []
items_b = []
for i in lines:
    a, b = i.split('   ')
    items_a.append(int(a))
    items_b.append(int(b))

items_a.sort()
items_b.sort()
res = 0
for i in range(len(items_a)):
    res += abs(items_a[i] - items_b[i])

print(res)
