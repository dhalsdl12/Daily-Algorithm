from collections import deque


def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    visit[0][0] = 1

    while queue:
        x, y, cnt = queue.popleft()
        if x + 1 == n and y + 1 == m:
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                if arr[nx][ny] == 0:
                    queue.appendleft((nx, ny, cnt))
                else:
                    queue.append((nx, ny, cnt + 1))


m, n = map(int, input().split())
arr = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visit = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    arr.append(list(map(int, input())))

print(bfs())