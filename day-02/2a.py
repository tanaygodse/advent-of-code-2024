with open("in") as f:
    lines = f.read().splitlines()

list_a = []
for i in lines:
    list_a.append(i.split(' '))

list_a = [[int(i) for i in l] for l in list_a]


def helper(l):
    minDiff = float('inf')
    maxDiff = float('-inf')
    for i in range(1, len(l)):
        minDiff = min(minDiff, abs(int(l[i]) - int(l[i-1])))
        maxDiff = max(maxDiff, abs(int(l[i]) - int(l[i-1])))

    return (minDiff, maxDiff)


res = 0
for l in list_a:
    if sorted(l) == l or sorted(l, reverse=True) == l:
        minDiff, maxDiff = helper(l)
    else:
        continue
    if minDiff <= 0 or maxDiff > 3:
        continue
    else:
        res += 1

print(res)
