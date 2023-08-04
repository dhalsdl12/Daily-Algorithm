from collections import deque


a, k = map(int, input().split())
visit = [-1 for _ in range(k + 1)]

queue = deque()
queue.append(a)
visit[a] = 0

while queue:
    n = queue.popleft()
    if n == k:
        print(visit[k])
        break

    if n + 1 <= k and visit[n + 1] == -1:
        visit[n + 1] = visit[n] + 1
        queue.append(n + 1)
    
    if n * 2 <= k and visit[n * 2] == -1:
        visit[n * 2] = visit[n] + 1
        queue.append(n * 2)