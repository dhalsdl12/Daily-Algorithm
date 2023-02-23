from collections import deque


def bfs(Dx, Dy):
    while queue:
        if arr[Dx][Dy] == 'S':
            return visit[Dx][Dy]
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i] 
            if 0 <= nx < r and 0 <= ny < c:
                if arr[x][y] == 'S' and (arr[nx][ny] == '.' or arr[nx][ny] == 'D'):
                    arr[nx][ny] = 'S'
                    visit[nx][ny] = visit[x][y] + 1
                    queue.append((nx, ny))
                elif arr[x][y] == '*' and (arr[nx][ny] == '.' or arr[nx][ny] == 'S'):
                    arr[nx][ny] = '*'
                    queue.append((nx, ny))
    return 'KAKTUS'


r, c = map(int, input().split())

arr = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
visit = [[0 for _ in range(c)] for _ in range(r)]


for i in range(r):
    s = list(input().strip())
    arr.append(s)
    for j in range(c):
        if s[j] == 'S':
            queue.append((i, j))
        elif s[j] == 'D':
            Dx, Dy = i, j

for i in range(r):
    for j in range(c):
        if arr[i][j] == '*':
            queue.append((i, j))

print(bfs(Dx,Dy))