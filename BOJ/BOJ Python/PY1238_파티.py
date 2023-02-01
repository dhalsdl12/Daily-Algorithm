import sys
import heapq


def dijkstra(start):
    dist = {node: sys.maxsize for node in graph}
    dist[start] = 0
    queue = []
    heapq.heappush(queue, (dist[start], start))
    while queue:
        cur_dist, node = heapq.heappop(queue)
        if dist[node] < cur_dist:
            continue
        for ad_node, d in graph[node].items():
            distance = d + cur_dist
            if dist[ad_node] > distance:
                dist[ad_node] = distance
                heapq.heappush(queue, (distance, ad_node))
    return dist


n, m, a = map(int, input().split())
graph = {}
for i in range(n):
    graph[i + 1] = {}
for i in range(m):
    x, y, d = map(int, input().split())
    graph[x][y] = d

Max = 0
come_dij = dijkstra(a)
for i in range(n):
    if i+1 == a:
        continue
    go_dij = dijkstra(i + 1)
    if Max < go_dij[a] + come_dij[i + 1]:
        Max = go_dij[a] + come_dij[i + 1]
print(Max)
