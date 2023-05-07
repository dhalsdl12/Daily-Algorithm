from collections import deque

def bfs():
    while queue:
        x, y = queue.popleft()

        if x == x2 and y == y2:
            return True
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if visit[nx][ny] == 0:
                    if arr[nx][ny] == '.':
                        queue.append((nx, ny))
                    else:
                        queue_tmp.append((nx, ny))
                    visit[nx][ny] = 1
    return False


def melt():
    while water:
        x, y = water.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if visit_melt[nx][ny] == 0:
                    if arr[nx][ny] == 'X':
                        water_tmp.append((nx, ny))
                        arr[nx][ny] = '.'
                    else:
                        water.append((nx, ny))
                    visit_melt[nx][ny] = 1


r, c = map(int, input().split())
arr = []
swan = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visit = [[0 for _ in range(c)] for _ in range(r)]
visit_melt = [[0 for _ in range(c)] for _ in range(r)]
cnt = 0

queue, queue_tmp = deque(), deque()
water, water_tmp = deque(), deque()

for i in range(r):
    tmp = list(input().strip())
    arr.append(tmp)
    for j in range(len(tmp)):
        if tmp[j] == 'L':
            swan.extend([i, j])
            water.append((i, j))
        if tmp[j] == '.':
            water.append((i, j))

x1, y1, x2, y2 = swan
arr[x1][y1] = '.'
arr[x2][y2] = '.'
visit[x1][y1] = 1
queue.append((x1, y1))

while True:
    if bfs():
        print(cnt)
        break
    melt()
    water = water_tmp
    queue = queue_tmp
    water_tmp = deque()
    queue_tmp = deque()
    cnt += 1