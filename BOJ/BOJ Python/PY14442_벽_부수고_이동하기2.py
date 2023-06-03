from collections import deque


def bfs():
    queue = deque()
    queue.append((0, 0, k, 1))
    visit[0][0][k] = 1

    while queue:
        x, y, b, cnt = queue.popleft()

        if x == n - 1 and y == m - 1:
            return cnt
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0 and visit[nx][ny][b] == 0:
                    queue.append((nx, ny, b, cnt + 1))
                    visit[nx][ny][b] = 1
                elif arr[nx][ny] == 1 and visit[nx][ny][b - 1] == 0:
                    if b > 0:
                        queue.append((nx, ny, b - 1, cnt + 1))
                        visit[nx][ny][b - 1] = 1 
    
    return -1


n, m, k = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().strip())))

visit = [[[0 for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs())