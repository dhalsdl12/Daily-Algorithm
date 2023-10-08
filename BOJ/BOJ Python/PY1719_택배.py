import heapq


def dijkstra(start):
    distance = [99999 for _ in range(n + 1)]
    distance[start] = 0
    parents, queue, result = {}, [], []
    heapq.heappush(queue, [distance[start], start])

    while queue:
        cd, cn = heapq.heappop(queue)

        if cd > distance[cn]:
            continue

        for nn, nd in arr[cn]:
            dist = nd + cd
            if dist < distance[nn]:
                distance[nn] = dist
                parents[nn] = cn
                heapq.heappush(queue, [dist, nn])
    
    for i in range(1, n + 1):
        if i == start:
            result.append('-')
        else:
            cur = i
            while True:
                if parents[cur] == start:
                    break
                cur = parents[cur]
            result.append(cur)
            
    return result


n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

for i in range(1, n + 1):
    answer = dijkstra(i)
    print(*answer)