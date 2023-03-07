from collections import deque


def bfs(i, j):
    queue = deque([((i, j))])
    visit[i][j] = 1
    country = []
    country.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if l <= abs(arr[nx][ny] - arr[x][y]) <= r:
                    visit[nx][ny] = 1
                    queue.append((nx, ny))
                    country.append((nx, ny))

    return country


n, l, r = map(int, input().split())
arr = []
answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    arr.append(list(map(int, input().split())))

while True:
    visit = [[0 for _ in range(n)] for _ in range(n)]
    check = 0

    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                country = bfs(i, j)

                if len(country) > 1:
                    check = 1
                    tmp = 0
                    for x, y in country:
                        tmp += arr[x][y]   
                    
                    tmp //= len(country)

                    for x, y in country:
                        arr[x][y] = tmp


    if check == 0:
        break
    answer += 1

print(answer)