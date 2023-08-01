from collections import deque

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((x, y))
    visit[x][y] = 1
    count = 0

    while queue:
        x, y = queue.popleft()

        if arr[x][y] == 'P':
            count += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
                if arr[nx][ny] != 'X':
                    queue.append((nx, ny))
                    visit[nx][ny] = 1

    return count


n, m = map(int, input().split())
visit = [[0 for _ in range(m)] for _ in range(n)]
arr = []
x, y = -1, -1
for i in range(n):
    li = list(input().rstrip())

    for j in range(m):
        if li[j] == 'I':
            x, y = i, j

    arr.append(li)

ans = bfs(x, y)
if ans == 0:
    print('TT')
else:
    print(ans)