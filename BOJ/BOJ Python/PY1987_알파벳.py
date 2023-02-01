dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, cnt):
    global result
    result = max(result, cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and \
                not maps[nx][ny] in alpha:
            alpha.add(maps[nx][ny])
            dfs(nx, ny, cnt + 1)
            alpha.remove(maps[nx][ny])


r, c = map(int, input().split())

maps = []
for i in range(r):
    maps.append(list(input()))

result = 0
alpha = set()
alpha.add(maps[0][0])

dfs(0, 0, 1)
print(result)
