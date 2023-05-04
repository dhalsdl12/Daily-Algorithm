from collections import deque


def bfs():
    queue = deque()
    queue.append((0, 0))
    visit[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
                if arr[nx][ny] >= 1:
                    arr[nx][ny] += 1
                else:
                    visit[nx][ny] = 1
                    queue.append((nx, ny))


n, m = map(int, input().split())
arr = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

for _ in range(n):
    arr.append(list(map(int, input().split())))


while True:
    check = 0
    visit = [[0 for _ in range(m)] for _ in range(n)]
    bfs()

    for i in range(n):
        for j in range(m):
            if arr[i][j] >= 3:
                arr[i][j] = 0
                check = 1
            elif arr[i][j] == 2:
                arr[i][j] = 1
    
    if check == 1:
        answer += 1
    else:
        break

print(answer)