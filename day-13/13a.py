with open('in') as f:
    lines = f.read().splitlines()

print(lines)

a_moves = []
b_moves = []
prizes = []
a_max = []
b_max = []

for l in lines:
    print(l)
    x = l.split(" ")
    if 'A:' in x:
        ax = x[-2].split("+")
        ay = x[-1].split("+")
        a_moves.append((int(ax[1][:-1]), int(ay[1])))
    if 'B:' in x:
        bx = x[-2].split("+")
        by = x[-1].split("+")
        b_moves.append((int(bx[1][:-1]), int(by[1])))
    if 'Prize:' in x:
        px = x[-2].split("=")
        py = x[-1].split("=")
        prizes.append((int(px[1][:-1]), int(py[1])))
        a_max.append(min(prizes[-1][0] // a_moves[-1]
                     [0], prizes[-1][1] // a_moves[-1][1]))
        b_max.append(min(prizes[-1][0] // b_moves[-1]
                     [0], prizes[-1][1] // b_moves[-1][1]))


print(a_moves)
print(b_moves)
print(a_max)
print(b_max)
print(prizes)
COST_A = 3
COST_B = 1
res = []
for i in range(len(a_moves)):
    flag = False
    for j in range(101):
        for k in range(101):
            if j * a_moves[i][0] + k * b_moves[i][0] == prizes[i][0] and j * a_moves[i][1] + k * b_moves[i][1] == prizes[i][1]:
                if j + k <= 200:
                    res.append(j*COST_A+k*COST_B)
                    flag = True
                    break
        if flag:
            break
    if not flag:
        res.append(-1)
print(res)
print(sum([r for r in res if r != -1]))
