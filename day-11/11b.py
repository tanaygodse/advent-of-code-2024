from collections import Counter

with open('in') as f:
    lines = f.read()
    stones = lines[:-1].split(" ")

print(stones)

stone_count = Counter(stones)

c = 0
while c < 75:
    new_count = Counter()
    for k in stone_count.keys():
        n = stone_count[k]
        if k == '0':
            new_count['1'] += n
        elif len(k) % 2 == 0:
            x = len(k) // 2
            first = str(int(k[:x]))
            second = str(int(k[x:]))
            new_count[first] += n
            new_count[second] += n
        else:
            new_count[str(int(k)*2024)] += n
    stone_count = new_count
    c += 1

print(sum(stone_count.values()))
