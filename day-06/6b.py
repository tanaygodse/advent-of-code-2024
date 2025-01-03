with open('in') as f:
    lines = f.read().splitlines()

adj_matrix = []

for i in lines:
    adj_matrix.append(list(i))

rows = len(adj_matrix)
cols = len(adj_matrix[0])

for r in range(rows):
    for c in range(cols):
        if adj_matrix[r][c] == '^':
            start_r, start_c = r, c
            break

res = 0
for r in range(rows):
    for c in range(cols):
        if adj_matrix[r][c] == '.':
            adj_matrix[r][c] = '#'
            visited_with_dir = set()
            cur_r, cur_c = start_r, start_c
            dir = 'up'

            while 0 <= cur_r < rows and 0 <= cur_c < cols:
                if (cur_r, cur_c, dir) in visited_with_dir:
                    res += 1
                    break
                visited_with_dir.add((cur_r, cur_c, dir))

                if dir == 'up':
                    nxt_r, nxt_c = cur_r - 1, cur_c
                elif dir == 'down':
                    nxt_r, nxt_c = cur_r + 1, cur_c
                elif dir == 'left':
                    nxt_r, nxt_c = cur_r, cur_c - 1
                elif dir == 'right':
                    nxt_r, nxt_c = cur_r, cur_c + 1

                if (0 <= nxt_r < rows and 0 <= nxt_c < cols) and adj_matrix[nxt_r][nxt_c] == '#':
                    if dir == 'up':
                        dir = 'right'
                    elif dir == 'right':
                        dir = 'down'
                    elif dir == 'down':
                        dir = 'left'
                    elif dir == 'left':
                        dir = 'up'
                else:
                    cur_r, cur_c = nxt_r, nxt_c

            adj_matrix[r][c] = '.'

print(res)
