from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visit[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0 and arr[nx][ny] == 1:
                queue.append((nx, ny))
                visit[nx][ny] = 1
                answer[nx][ny] = answer[x][y] + 1


n, m = map(int, input().split())
arr = []
answer = [[-1 for _ in range(m)] for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]
x, y = -1, -1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    li = list(map(int, input().split()))

    for j in range(m):
        if li[j] == 2:
            x, y = i, j
            answer[i][j] = 0
    
        if li[j] == 0:
            answer[i][j] = 0

    arr.append(li)

bfs(x, y)

for ans in answer:
    print(*ans)