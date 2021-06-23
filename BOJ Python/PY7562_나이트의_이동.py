from collections import deque

case = int(input())
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

for i in range(case):
    queue = deque()
    size = int(input())
    visit = [[0] * size for i in range(size)]
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    queue.append([x1, y1])
    visit[x1][y1] = 1
    while queue:
        a, b = queue[0][0], queue[0][1]
        queue.popleft()
        if a == x2 and b == y2:
            print(visit[a][b]-1)
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < size and 0 <= y < size and visit[x][y] == 0:
                queue.append([x, y])
                visit[x][y] = visit[a][b] + 1