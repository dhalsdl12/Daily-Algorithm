from collections import deque


def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    visit[0][0] = 1

    while queue:
        x, y, cnt = queue.popleft()

        if x == n - 1 and y == n - 1:
            return cnt
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if arr[nx][ny] == 1:
                    queue.appendleft((nx, ny, cnt))
                    visit[nx][ny] = 1
                else:
                    queue.append((nx, ny, cnt + 1))
                    visit[nx][ny] = 1


n = int(input())
arr = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visit = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    arr.append(list(map(int, input().strip())))

print(bfs())