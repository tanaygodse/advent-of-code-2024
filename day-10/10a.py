with open('in') as f:
    lines = f.read().splitlines()

print(lines)

adj_matrix = []

for l in lines:
    adj_matrix.append([int(i) for i in l])

print(adj_matrix)

rows = len(adj_matrix)
cols = len(adj_matrix[0])

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(r, c, val, visited):
    if adj_matrix[r][c] != val:
        return 0
    if val == 0:
        return 1
    res = 0
    for dr, dc in dirs:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and adj_matrix[nr][nc] == val - 1:
            visited.add((nr, nc))
            res += dfs(nr, nc, val-1, visited)
    return res


paths = 0
for r in range(rows):
    for c in range(cols):
        if adj_matrix[r][c] == 9:
            paths += dfs(r, c, adj_matrix[r][c], set())

print(paths)
