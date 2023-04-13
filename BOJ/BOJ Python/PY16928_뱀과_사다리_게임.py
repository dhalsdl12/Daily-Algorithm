from collections import deque


def bfs():
    queue = deque()
    queue.append((1, 0))
    visit = [0 for _ in range(101)]
    visit[1] = 1

    while queue:
        x, cnt = queue.popleft()
        if x == 100:
            return cnt
        for i in range(1, 7, 1):
            nx = x + i

            if 0 < nx <= 100 and visit[nx] == 0:
                if nx in dic_a:
                    nx = dic_a[nx]
                if nx in dic_b:
                    nx = dic_b[nx]
                
                if visit[nx] == 0:
                    queue.append((nx, cnt + 1))
                    visit[nx] = 1



n, m = map(int, input().split())
dic_a = {}
dic_b = {}

for i in range(n):
    x, y = map(int, input().split())
    dic_a[x] = y

for i in range(m):
    u, v = map(int, input().split())
    dic_b[u] = v

print(bfs())