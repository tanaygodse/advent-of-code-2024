from collections import defaultdict, deque
with open("in") as f:
    lines = f.read().splitlines()

# print(lines)

nums = []
for i in lines[0]:
    nums.append(int(i))

counts = defaultdict(int)
storage = []
block = 0
for i in range(0, len(nums)):
    if i % 2 == 0:
        for j in range(nums[i]):
            storage.append(block)
        counts[block] = nums[i]
        block += 1
    else:
        for j in range(nums[i]):
            storage.append(-1)


t = block
while t > 0:
    c = counts[t]
    if c == 0:
        t -= 1
        continue
    spaces = 0
    for i in range(len(storage)):
        # break if storage loop has reached the block we are trying to move, ie didnt find space
        if storage[i] == t:
            break
        # count space, if count of block is able to fit, move it, else if spaces are less than count, check next block
        if storage[i] == -1:
            spaces += 1
        else:
            spaces = 0

        if spaces >= c:
            # set to -1 after moving
            for j in range(len(storage)):
                if storage[j] == t:
                    storage[j] = -1
            # set the spaces to block
            for j in range(c):
                storage[i-j] = t
            break
    t -= 1

res = 0
for i, n in enumerate(storage):
    if n != -1:
        res += i * n
print(res)
