with open("in") as f:
    lines = f.read()

lines = lines.split('\n\n')
original_grid = [list(l) for l in lines[0].splitlines()]
moves = lines[1].strip()

# Resizing the grid for Part 2


def resize_grid(grid):
    new_grid = []
    for row in grid:
        new_row = []
        for tile in row:
            if tile == '#':
                new_row.extend(['#', '#'])
            elif tile == 'O':
                new_row.extend(['[', ']'])
            elif tile == '.':
                new_row.extend(['.', '.'])
            elif tile == '@':
                new_row.extend(['@', '.'])
        new_grid.append(new_row)
    return new_grid


grid = resize_grid(original_grid)
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


def isBlocked(x, y, dx, dy, seen):
    if (x, y) in seen:
        return
    if grid[x][y] == '#':
        return True
    if grid[x][y] == ".":
        return False
    seen.add((x, y))
    if grid[x][y] == "[":
        if dx:
            return isBlocked(x, y+1, dx, dy, seen) or isBlocked(x+dx, y+dy, dx, dy, seen) or isBlocked(x+dx, y+dy+1, dx, dy, seen)
        else:
            return isBlocked(x+dx, y+dy, dx, dy, seen)
    elif grid[x][y] == "]":
        if dx:
            return isBlocked(x, y-1, dx, dy, seen) or isBlocked(x+dx, y+dy, dx, dy, seen) or isBlocked(x+dx, y+dy-1, dx, dy, seen)
        else:
            return isBlocked(x+dx, y+dy, dx, dy, seen)


def moveBox(x, y, dx, dy, item):
    if grid[x][y] == ".":
        grid[x][y] = item
    elif grid[x][y] == "[":
        grid[x][y] = item
        grid[x][y+1] = "."
        moveBox(x+dx, y+dy, dx, dy, "[")
        moveBox(x+dx, y+dy+1, dx, dy, "]")
    elif grid[x][y] == "]":
        grid[x][y] = item
        grid[x][y-1] = "."
        moveBox(x+dx, y+dy, dx, dy, "]")
        moveBox(x+dx, y+dy-1, dx, dy, "[")


for m in moves:
    print(m)
    dx, dy = dirs[m]
    nx, ny = cur_x + dx, cur_y + dy
    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not isBlocked(nx, ny, dx, dy, set()):
        print("nx, ny:", nx, ny, grid[nx][ny])
        grid[cur_x][cur_y] = "."
        cur_x, cur_y = nx, ny
        moveBox(cur_x, cur_y, dx, dy, "@")
    print("\n".join(["".join(x) for x in grid]))

res = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '[':
            res += 100 * i + j
print(res)
