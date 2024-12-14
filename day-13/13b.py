import numpy as np

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
        prizes.append((int(px[1][:-1]) + 10000000000000,
                      int(py[1]) + 10000000000000))
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
res = 0
for i in range(len(a_moves)):
    a, b = a_moves[i]
    c, d = b_moves[i]
    e, f = prizes[i]
    A = np.array([[a, c], [b, d]])
    B = np.array([e, f])
    x = np.linalg.solve(A, B)
    t = [int(round(x[0])), int(round(x[1]))]
    if t[0] * a + t[1] * c == e and t[0] * b + t[1] * d == f:
        res += t[0] * COST_A + t[1] * COST_B


print(res)
