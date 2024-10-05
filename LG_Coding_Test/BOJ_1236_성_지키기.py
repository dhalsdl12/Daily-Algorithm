n, m = map(int, input().split())
col = [0 for _ in range(m)]
row = [0 for _ in range(n)]
row_cnt, col_cnt = 0, 0

for i in range(n):
    s = input()

    for j in range(m):
        c = s[j]

        if c == 'X':
            row[i] = 1
            col[j] = 1

for r in row:
    if r == 0:
        row_cnt += 1

for c in col:
    if c == 0:
        col_cnt += 1

print(max(row_cnt, col_cnt))