from collections import deque


def solution(n, edge):
    arr = [[] for _ in range(n + 1)]
    visit = [0 for _ in range(n + 1)]
    for a, b in edge:
        arr[a].append(b)
        arr[b].append(a)
    
    queue = deque()
    queue.append(1)
    visit[1] = 1
    
    while queue:
        cur = queue.popleft()
        for node in arr[cur]:
            if visit[node] == 0:
                visit[node] = visit[cur] + 1
                queue.append(node)
    
    Max = max(visit)
    
    return visit.count(Max)