from collections import deque


def bfs(a, b):
    queue = deque([(a, b)])
    visit[a][b] = 1
    melt_list = []

    while queue:
        x, y = queue.popleft()
        melt = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0:
                    melt += 1
                elif arr[nx][ny] != 0 and visit[nx][ny] == 0:
                    queue.append((nx, ny))
                    visit[nx][ny] = 1
        if melt > 0:
            melt_list.append((x, y, melt))
    
    for x, y, melt in melt_list:
        arr[x][y] = max(0, arr[x][y] - melt)

    return 1


n, m = map(int, input().split())

year = 0
arr, ice = [], []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
    
    for j in range(m):
        if a[j] != 0:
            ice.append((i, j))

while ice:
    visit = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
    melt = []

    for i, j in ice:
        if arr[i][j] != 0 and visit[i][j] == 0:
            count += bfs(i, j)
        if arr[i][j] == 0:
            melt.append((i, j))
    if count > 1:
        print(year)
        break

    ice = sorted(list(set(ice) - set(melt)))
    year += 1

if count < 2:
    print(0)
