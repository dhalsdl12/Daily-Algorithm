from collections import deque
import sys
sys.setrecursionlimit(10**6)


def dfs(x, weight):
    for a, b in graph[x]:
        if dist[a] == -1:
            dist[a] = b + weight
            dfs(a, weight + b)


n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(n):
    arr = deque(list(map(int, input().split())))
    a = arr.popleft()

    while True:
        b = arr.popleft()
        w = arr.popleft()

        graph[a].append([b, w])
        graph[b].append([a, w])

        if len(arr) == 1:
            break

dist = [-1 for _ in range(n + 1)]
dist[1] = 0
dfs(1, 0)

tmp = dist.index(max(dist))
dist = [-1 for _ in range(n + 1)]
dist[tmp] = 0
dfs(tmp, 0)

print(max(dist))