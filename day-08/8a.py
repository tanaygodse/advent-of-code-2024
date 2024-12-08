from collections import defaultdict

with open("in") as f:
    lines = f.read().splitlines()

print(lines)

rows = len(lines)
cols = len(lines[0])

placed = set()

distances = defaultdict(list)

for i in range(rows):
    for j in range(cols):
        if lines[i][j] != '.':
            distances[lines[i][j]].append((i, j))

print(distances)
for k, v in distances.items():
    print(k)
    for i, v1 in enumerate(v):
        x1, y1 = v1
        print("x1, y1", x1, y1)
        for j, v2 in enumerate(v[i+1:]):
            x2, y2 = v2
            print("x2, y2", x2, y2)
            if x2 > x1:
                if y2 > y1:
                    dx = x2 - x1
                    dy = y2 - y1
                    nx = x1 - dx
                    ny = y1 - dy
                    print(nx, ny)
                    if (nx, ny) not in placed and 0 <= nx < rows and 0 <= ny < cols:
                        placed.add((nx, ny))
                    nx = x2 + dx
                    ny = y2 + dy
                    print(nx, ny)
                    if (nx, ny) not in placed and 0 <= nx < rows and 0 <= ny < cols:
                        placed.add((nx, ny))
                else:
                    dx = x2 - x1
                    dy = y1 - y2
                    nx = x1 - dx
                    ny = y1 + dy
                    print(nx, ny)
                    if (nx, ny) not in placed and 0 <= nx < rows and 0 <= ny < cols:
                        placed.add((nx, ny))
                    nx = x2 + dx
                    ny = y2 - dy
                    print(nx, ny)
                    if (nx, ny) not in placed and 0 <= nx < rows and 0 <= ny < cols:
                        placed.add((nx, ny))
            else:
                if y2 > y1:
                    dx = x1 - x2
                    dy = y2 - y1
                    nx = x1 + dx
                    ny = y1 - dy
                    if (nx, ny) not in placed and 0 <= nx < rows and 0 <= ny < cols:
                        placed.add((nx, ny))
                    nx = x2 - dx
                    ny = y2 + dy
                    if (nx, ny) not in placed and 0 <= nx < rows and 0 <= ny < cols:
                        placed.add((nx, ny))
                else:
                    dx = x1 - x2
                    dy = y1 - y2
                    nx = x1 + dx
                    ny = y1 + dy
                    if (nx, ny) not in placed and 0 <= nx < rows and 0 <= ny < cols:
                        placed.add((nx, ny))
                    nx = x2 - dx
                    ny = y2 - dy
                    if (nx, ny) not in placed and 0 <= nx < rows and 0 <= ny < cols:
                        placed.add((nx, ny))
            print('------')
print(sorted([(x, y) for x, y in placed]))
print(len(placed))
