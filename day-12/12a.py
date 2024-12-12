from collections import defaultdict

with open('in') as f:
    lines = f.read().splitlines()

print(lines)

adj_mat = []

for i in lines:
    adj_mat.append([l for l in i])

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


rows, cols = len(lines), len(lines[0])


seen = set()


def getMeasurements(r, c, ch, visited):
    visited.add((r, c))
    seen.add((r, c))
    peri = 0
    ar = 1
    for dr, dc in dirs:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
            if adj_mat[nr][nc] != ch:
                peri += 1
            if adj_mat[nr][nc] == ch:
                p, a = getMeasurements(nr, nc, ch, visited)
                ar += a
                peri += p
        else:
            if nr == -1 or nc == -1 or nr == rows or nc == rows:
                peri += 1
    return (peri, ar)


perimeter = {}
area = {}
for i in range(rows):
    for j in range(cols):
        if (i, j) not in seen:
            p, a = getMeasurements(i, j, adj_mat[i][j], set())
            perimeter[f"{i}, {j}"] = p
            area[f"{i}, {j}"] = a


print("area")
print(area)
print("perimeter")
print(perimeter)

res = 0
for k in perimeter:
    res += perimeter[k] * area[k]


print(res)
