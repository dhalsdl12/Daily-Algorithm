import sys
import heapq


def dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap, [0, start])
    while heap:
        wei, now = heapq.heappop(heap)

        if dp[now] < wei:
            continue
        for we, next_node in graph[now]:
            next_wei = we + wei
            if next_wei < dp[next_node]:
                dp[next_node] = next_wei
                heapq.heappush(heap, [next_wei, next_node])


v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v+1)]
dp = [sys.maxsize]*(v+1)
heap = []


for i in range(e):
    u, v, w = map(int, input().split())
    graph[u].append([w, v])

dijkstra(k)
for i in dp[1:]:
    if i == sys.maxsize:
        print("INF")
    else:
        print(i)