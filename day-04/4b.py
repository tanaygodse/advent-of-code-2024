with open("in") as f:
    lines = f.read().splitlines()

adj_mat = []
for i in lines:
    adj_mat.append(list(i))

word = "MAS"


def is_xmas(r, c):
    if adj_mat[r-1][c-1] == word[0] and adj_mat[r+1][c+1] == word[2] and adj_mat[r-1][c+1] == word[0] and adj_mat[r+1][c-1] == word[2]:
        return True
    if adj_mat[r-1][c-1] == word[0] and adj_mat[r+1][c+1] == word[2] and adj_mat[r-1][c+1] == word[2] and adj_mat[r+1][c-1] == word[0]:
        return True
    if adj_mat[r-1][c-1] == word[2] and adj_mat[r+1][c+1] == word[0] and adj_mat[r-1][c+1] == word[0] and adj_mat[r+1][c-1] == word[2]:
        return True
    if adj_mat[r-1][c-1] == word[2] and adj_mat[r+1][c+1] == word[0] and adj_mat[r-1][c+1] == word[2] and adj_mat[r+1][c-1] == word[0]:
        return True
    return False


res = 0
rows = len(adj_mat)
cols = len(adj_mat[0])
for r in range(rows):
    for c in range(cols):
        if 0 <= r - 1 < rows and 0 <= r + 1 < rows and 0 <= c - 1 < cols and 0 <= c + 1 < cols:
            if adj_mat[r][c] == word[1]:
                if is_xmas(r, c):
                    res += 1

print(res)
