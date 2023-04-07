from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visit[x][y] = 1
    color = arr[x][y]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if arr[nx][ny] == color:
                    visit[nx][ny] = 1
                    queue.append((nx, ny))      


n = int(input())
arr = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt_a, cnt_b = 0, 0

for i in range(n):
    arr.append(list(input().rstrip()))

visit = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            bfs(i, j)
            cnt_a += 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

visit = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            bfs(i, j)
            cnt_b += 1

print(cnt_a, cnt_b)