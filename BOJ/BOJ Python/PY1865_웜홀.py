def bellman_ford(start):
    dist[start] = 0

    for i in range(1, n + 1):
        for node in range(1, n + 1):
            for nn, time in graph[node]:
                if dist[nn] > dist[node] + time:
                    dist[nn] = dist[node] + time
                    if i == n:
                        return True
                    
    return False


tc = int(input())
answer = []

for _ in range(tc):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    dist = [99999 for _ in range(n + 1)]

    for _ in range(m):
        s, e, t = map(int, input().split())
        graph[s].append([e, t])
        graph[e].append([s, t])
    
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph[s].append([e, -t])
    

    if bellman_ford(1):
        answer.append('YES')
    else:
        answer.append('NO')

for ans in answer:
    print(ans)