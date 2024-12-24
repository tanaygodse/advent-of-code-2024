with open("in") as f:
    lines = f.read()

print(lines)
lines = lines.split('\n\n')

grid = [list(l) for l in lines[0].splitlines()]

moves = lines[1][:-1]

print(moves)

start_x, start_y = 0, 0
grid = [g for g in grid]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "@":
            cur_x, cur_y = i, j

print(grid)

moves = moves.replace("\n", "")
print(moves)

dirs = {">": (0, 1), "v": (1, 0), "^": (-1, 0), "<": (0, -1)}


def isBlocked(x, y, dx, dy):
    print("isBlocked, x, y", x, y, grid[x][y])
    if grid[x][y] == '#':
        return True
    if grid[x][y] == ".":
        return False
    return isBlocked(x+dx, y+dy, dx, dy)


def moveBox(x, y, dx, dy, item):
    if grid[x][y] == ".":
        grid[x][y] = item
    elif grid[x][y] == "O":
        grid[x][y] = item
        moveBox(x+dx, y+dy, dx, dy, "O")


for m in moves:
    print(m)
    dx, dy = dirs[m]
    nx, ny = cur_x + dx, cur_y + dy
    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not isBlocked(nx, ny, dx, dy):
        print("nx, ny:", nx, ny, grid[nx][ny])
        grid[cur_x][cur_y] = "."
        cur_x, cur_y = nx, ny
        moveBox(cur_x, cur_y, dx, dy, "@")

res = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'O':
            res += 100 * i + j
print(res)
