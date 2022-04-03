from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
d1 = [-2, -2, -1, -1, 1, 1, 2, 2]
d2 = [1, -1, 2, -2, 2, -2, 1, -1]


def bfs():
    que = deque()
    que.append((0, 0, k))
    visit = [[[0 for L in range(31)] for M in range(w)] for N in range(h)]

    while que:
        x, y, k1 = que.popleft()

        if x == h-1 and y == w-1:
            return visit[x][y][k1]

        for cnt in range(4):
            x1 = x + dx[cnt]
            y1 = y + dy[cnt]

            if 0 <= x1 < h and 0 <= y1 < w:
                if Map[x1][y1] != 1 and visit[x1][y1][k1] == 0:
                    visit[x1][y1][k1] = visit[x][y][k1] + 1
                    que.append((x1, y1, k1))
        if k1 > 0:
            for cnt in range(8):
                x1 = x + d1[cnt]
                y1 = y + d2[cnt]

                if 0 <= x1 < h and 0 <= y1 < w:
                    if Map[x1][y1] != 1 and visit[x1][y1][k1-1] == 0:
                        visit[x1][y1][k1-1] = visit[x][y][k1] + 1
                        que.append((x1, y1, k1-1))
    return -1


k = int(input())
w, h = map(int, input().split())
Map = []

for i in range(h):
    Map.append(list(map(int, input().split())))

print(bfs())
