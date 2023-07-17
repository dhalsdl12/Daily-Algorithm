from collections import deque
import sys
sys.setrecursionlimit(10**9)


def dfs(s, e, cnt, tmp):
    global check
    for nx in station[e]:
        if nx == s and cnt > 2:
            for t in tmp:
                cycle.append(t)
            check = True

        if visit[nx] == -1:
            visit[nx] = 1
            dfs(s, nx, cnt + 1, tmp + [nx])
            visit[nx] = -1
        

def bfs():
    queue = deque()
    visit = [-1 for _ in range(n + 1)]

    for c in cycle:
        queue.append((c, 0))
        visit[c] = 0

    while queue:
        x, cnt = queue.popleft()

        for nx in station[x]:
            if visit[nx] == -1:
                visit[nx] = cnt + 1
                queue.append((nx, cnt + 1))
    
    return visit


n =  int(input())
station = [[] for _ in range(n + 1)]
visit = [-1 for _ in range(n + 1)]
cycle = []
check = False

for i in range(n):
    a, b = map(int, input().split())
    station[a].append(b)
    station[b].append(a)
                
for i in range(1, n + 1):
    if check == True:
        break
    visit[i] = 1
    dfs(i, i, 1, [i])
    visit[i] = -1

print(*bfs()[1:])