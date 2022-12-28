from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    while que:
        x, y, key, cnt = que.popleft()
        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]

            if 0 <= x1 < n and 0 <= y1 < m and Map[x1][y1] != '#' and visit[x1][y1][key] == 0:
                if Map[x1][y1] == '1':
                    return cnt + 1
                elif Map[x1][y1] == '.':
                    visit[x1][y1][key] = 1
                    que.append([x1, y1, key, cnt+1])
                else:
                    if Map[x1][y1].isupper():
                        keychar = ord(Map[x1][y1]) - 65
                        if key & 1 << keychar:
                            visit[x1][y1][key] = 1
                            que.append([x1, y1, key, cnt+1])
                    elif Map[x1][y1].islower():
                        keychar = ord(Map[x1][y1]) - 97
                        sumkey = key | (1 << keychar)
                        if visit[x1][y1][sumkey] == 0:
                            visit[x1][y1][sumkey] = 1
                            que.append([x1, y1, sumkey, cnt+1])
    return -1


n, m = map(int, input().split())
visit = [[[0] * 64 for i in range(m)] for i in range(n)]
que = deque()
Map = []

for i in range(n):
    Map.append(list(input().strip()))
    for j in range(m):
        if Map[i][j] == '0':
            que.append([i, j, 0, 0])
            Map[i][j] = '.'
            visit[i][j][0] = 1
print(bfs())
