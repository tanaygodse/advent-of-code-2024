with open("in") as f:
    lines = f.read().splitlines()


adj_mat = []
for i in lines:
    adj_mat.append(list(i))

dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


word = "XMAS"


def dfs(r, c, i, rd=None, cd=None):
    if adj_mat[r][c] != word[i]:
        return 0
    if i == len(word) - 1:
        return 1
    cnt = 0
    if rd is not None and cd is not None:
        if 0 <= r + rd < rows and 0 <= c + cd < cols:
            cnt += dfs(r+rd, c+cd, i + 1, rd, cd)
    else:
        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                cnt += dfs(nr, nc, i+1, dr, dc)
    return cnt


res = 0
rows = len(adj_mat)
cols = len(adj_mat[0])
for r in range(rows):
    for c in range(cols):
        if adj_mat[r][c] == word[0]:
            res += dfs(r, c, 0)

print(res)
