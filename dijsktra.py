import heapq


def dijsktra(start):
    distance = [999999 for _ in range(7)]
    distance[start] = 0
    queue = []

    heapq.heappush(queue, [distance[start], start])

    while queue:
        cur_distance, cur_node = heapq.heappop(queue)

        if distance[cur_node] < cur_distance:
            continue

        for n_node, n_distance in arr[cur_node]:
            dist = cur_distance + n_distance

            if dist < distance[n_node]:
                distance[n_node] = dist
                heapq.heappush(queue, [distance[n_node], n_node])
    
    return distance


graph = {
    1: {2: 8, 3: 1, 4: 2},
    2: {},
    3: {2: 5, 4: 2},
    4: {5: 3, 6: 5},
    5: {6: 1},
    6: {1: 5}
}

arr = [[] for _ in range(7)]

for a, b in graph.items():
    for c, d in b.items():
        arr[a].append((c, d))

distance = dijsktra(1)

for d in distance:
    print(d)