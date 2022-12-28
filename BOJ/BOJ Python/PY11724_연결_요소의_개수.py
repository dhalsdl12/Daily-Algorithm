import sys
sys.setrecursionlimit(10000)

def dfs(v):
    visit[v] = True
    for e in arr[v]:
        if visit[e] == False:
            dfs(e)


n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
visit = [False]*(n+1)
cnt = 0

for i in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
for i in range(1, n+1):
    if visit[i] == False:
        dfs(i)
        cnt += 1

print(cnt)
