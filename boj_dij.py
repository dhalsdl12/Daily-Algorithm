import heapq

def dijkstra(start):
    distance = [99999 for _ in range(n + 1)]
    distance[start] = 0
    queue = []

    heapq.heappush(queue, [distance[start], start])

    while queue:
        cd, cn = heapq.heappop(queue)

        if cd > distance[cn]:
            continue

        for nn, nd in arr[cn]:
            dist = nd + cd
            if dist < distance[nn]:
                distance[nn] = dist
                heapq.heappush(queue, [dist, nn])
        
    return distance


n, m, x = map(int, input().split())
arr = [[] for _ in range(n + 1)]
answer = 0
for i in range(m):
    a, b, t = map(int, input().split())
    arr[a].append((b, t))

dist = dijkstra(x)
for i in range(n):
    dist2 = dijkstra(i + 1)[x]
    dist3 = dist[i + 1]

    answer = max(answer, dist2 + dist3)
print(answer)
