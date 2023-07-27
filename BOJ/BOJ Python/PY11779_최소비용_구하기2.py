import heapq
import sys
input = sys.stdin.readline


def dijk(start):
    queue = [(0, start)]
    dist[start] = 0

    while queue:
        weight, node = heapq.heappop(queue)
        if weight > dist[node]:
            continue

        for nn, nw in graph[node]:
            cost = weight + nw
            
            if cost < dist[nn]:
                dist[nn] = cost
                prev[nn] = node
                heapq.heappush(queue, (cost, nn))


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])

start, end = map(int, input().split())
dist = [1e9 for _ in range(n + 1)]
prev = [0 for _ in range(n + 1)]

dijk(start)
print(dist[end])

answer = [end]
node = end

while True:
    node = prev[node]
    answer.append(node)

    if node == start:
        break

print(len(answer))
print(*answer[::-1])