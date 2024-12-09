from collections import Counter

with open("in") as f:
    lines = f.read().splitlines()

items_a = []
items_b = []

for i in lines:
    a, b = i.split('   ')
    items_a.append(int(a))
    items_b.append(int(b))


dict_b = Counter(items_b)

res = 0
for i in range(len(items_a)):
    res += items_a[i] * dict_b.get(items_a[i], 0)

print(res)
