from collections import deque


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visit[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1:
                if visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    queue.append((nx, ny))


answer = []
dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    arr = []
    visit = [[0 for _ in range(w)] for _ in range(h)]
    count = 0

    for _ in range(h):
        arr.append(list(map(int, input().split())))
    
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 0 or visit[i][j] == 1:
                continue
            bfs(i, j)
            count += 1
            
    answer.append(count)

for ans in answer:
    print(ans)
            