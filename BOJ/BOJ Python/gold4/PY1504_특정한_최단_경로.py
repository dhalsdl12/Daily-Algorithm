import sys
import heapq


def dijkstra(start):
    dp = [sys.maxsize for i in range(n+1)]
    dp[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])

    while heap:
        w, c = heapq.heappop(heap)

        for next_node, next_weight in s[c]:
            weight = next_weight + w
            if dp[next_node] > weight:
                dp[next_node] = weight
                heapq.heappush(heap, [weight, next_node])
    return dp


n, e = map(int, sys.stdin.readline().split())

s = [[] for _ in range(n+1)]

for i in range(e):
    a, b, w = map(int, sys.stdin.readline().split())
    s[a].append([b, w])
    s[b].append([a, w])

v1, v2 = map(int, sys.stdin.readline().split())

first = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)

result = min(first[v1]+v1_[v2]+v2_[n], first[v2]+v2_[v1]+v1_[n])

if result < sys.maxsize:
    print(result)
else:
    print(-1)
