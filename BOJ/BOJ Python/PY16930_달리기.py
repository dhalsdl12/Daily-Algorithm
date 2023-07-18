from collections import deque


def bfs():
    queue = deque()
    queue.append([x1 - 1, y1 - 1])

    while queue:
        x, y = queue.popleft()
        if x == x2 - 1 and y == y2 - 1:
            return visit[x][y]
        
        for i in range(4):
            for num in range(1, k + 1):
                nx = x + dx[i] * num
                ny = y + dy[i] * num
                
                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == '.':
                    if visit[nx][ny] == 0:
                        visit[nx][ny] = visit[x][y] + 1
                        queue.append([nx, ny])
                    elif visit[nx][ny] == visit[x][y] + 1:
                        continue
                    else:
                        break
                else:
                    break
    
    return -1


n, m, k = map(int, input().split())
arr = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visit = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    arr.append(list(input().rstrip()))

x1, y1, x2, y2 = map(int, input().split())
print(bfs())