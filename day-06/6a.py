inp = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''


adj_matrix = []

for i in inp.split('\n'):
    adj_matrix.append(list(i))


rows = len(adj_matrix)
cols = len(adj_matrix[0])

visited = set()


def start_moving(r, c, dir):
    if dir == 'up':
        for i in range(r, -1, -1):
            if adj_matrix[i][c] != '#':
                visited.add((i, c))
            else:
                return start_moving(i+1, c, 'right')
    elif dir == 'down':
        for i in range(r+1, rows):
            if adj_matrix[i][c] != '#':
                visited.add((i, c))
            else:
                return start_moving(i-1, c, 'left')
    elif dir == 'left':
        for j in range(c, -1, -1):
            if adj_matrix[r][j] != '#':
                visited.add((r, j))
            else:
                return start_moving(r, j+1, 'up')
    elif dir == 'right':
        for j in range(c+1, cols):
            if adj_matrix[r][j] != '#':
                visited.add((r, j))
            else:
                return start_moving(r, j-1, 'down')
    return


for r in range(rows):
    for c in range(cols):
        if adj_matrix[r][c] == '^':
            start_moving(r, c, 'up')

print(len(visited))
