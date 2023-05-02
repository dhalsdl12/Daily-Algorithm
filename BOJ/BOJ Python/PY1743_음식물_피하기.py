from collections import deque


def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    visit[a][b] = 1
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    queue.append((nx, ny))
                    cnt += 1

    return cnt


n, m, k = map(int, input().split())

arr = [[0 for _ in range(m)] for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

for i in range(k):
    r, c = map(int, input().split())
    arr[r - 1][c - 1] = 1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visit[i][j] == 0:
            tmp = bfs(i, j)
            answer = max(answer, tmp)

print(answer)