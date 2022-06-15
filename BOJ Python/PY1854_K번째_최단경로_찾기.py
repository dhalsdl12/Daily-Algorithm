import sys
import heapq


def dijkstra(start):
    dp[start][0] = 0
    queue = []
    heapq.heappush(queue, [0, start])
    while queue:
        cur_dist, node = heapq.heappop(queue)
        for ad_node, d in graph[node]:
            w_dist = cur_dist + d
            if w_dist < dp[ad_node][k - 1]:
                dp[ad_node][k-1] = w_dist
                dp[ad_node].sort()
                heapq.heappush(queue, [w_dist, ad_node])


n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dp = [[sys.maxsize] * k for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
dijkstra(1)

for i in range(1, n + 1):
    if dp[i][k-1] == sys.maxsize:
        print(-1)
    else:
        print(dp[i][k-1])
