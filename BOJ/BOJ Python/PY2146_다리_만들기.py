from collections import deque


def bfs_island(i, j):
    queue = deque()
    queue.append([i, j])

    visit[i][j] = 1
    arr[i][j] = count

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and arr[nx][ny] == 1:
                visit[nx][ny] = 1
                arr[nx][ny] = count
                queue.append([nx, ny])


def bfs(c):
    dist = [[-1 for _ in range(n)] for _ in range(n)]
    queue = deque()

    for i in range(n):
        for j in range(n):
            if arr[i][j] == c:
                queue.append([i, j])
                dist[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] != 0 and arr[nx][ny] != c:
                    return dist[x][y]
                if arr[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append([nx, ny])


n  = int(input())
arr = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visit = [[0 for _ in range(n)] for _ in range(n)]
count = 1
answer = 99999

for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if visit[i][j] == 0 and arr[i][j] == 1:
            bfs_island(i, j)
            count += 1

for i in range(1, count):
    tmp = bfs(i)
    answer = min(answer, tmp)

print(answer)