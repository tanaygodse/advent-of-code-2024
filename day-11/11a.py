with open('in') as f:
    lines = f.read()
    stones = lines[:-1].split(" ")

print(stones)

flag = False
prevStones = []

c = 0
while c < 25:
    if prevStones == []:
        for i in range(len(stones)):
            if stones[i] == '0':
                prevStones.append('1')
            elif len(stones[i]) % 2 == 0:
                x = len(stones[i]) // 2
                first = stones[i][:x]
                second = stones[i][x:]
                prevStones.append(str(int(first)))
                prevStones.append(str(int(second)))
            else:
                prevStones.append(str(int(stones[i])*2024))
    else:
        newPrev = []
        for i in range(len(prevStones)):
            if prevStones[i] == '0':
                newPrev.append('1')
            elif len(prevStones[i]) % 2 == 0:
                x = len(prevStones[i]) // 2
                first = prevStones[i][:x]
                second = prevStones[i][x:]
                newPrev.append(str(int(first)))
                newPrev.append(str(int(second)))
            else:
                newPrev.append(str(int(prevStones[i])*2024))
        prevStones = newPrev
    print(prevStones)
    c += 1

print(len(prevStones))
