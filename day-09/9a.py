from collections import deque
with open("in") as f:
    lines = f.read().splitlines()

# print(lines)

nums = []
for i in lines[0]:
    nums.append(int(i))


storage = []
block = 0
for i in range(0, len(nums)):
    if i % 2 == 0:
        for j in range(nums[i]):
            storage.append(block)
        block += 1
    else:
        for j in range(nums[i]):
            storage.append(-1)

q = deque(storage)

i = 0
while i < len(storage):
    if storage[i] == -1:
        while storage[i] == -1:
            storage[i] = q.pop()
            storage = storage[:-1]
    i += 1
res = 0
for i, n in enumerate(storage):
    res += i * n
print(res)
