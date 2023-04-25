from collections import deque


def bfs():
    queue = deque()
    queue.append((1, 0, 0))
    visit[1][0] = 1
    while queue:
        s, clip, time = queue.popleft()
        if s == n:
            return time
        
        if visit[s][s] == 0:
            visit[s][s] = 1
            queue.append((s, s, time + 1))
        if s + clip <= n and visit[s + clip][clip] == 0:
            visit[s + clip][clip] = 1
            queue.append((s + clip, clip, time + 1))
        if s - 1 >= 0 and visit[s - 1][clip] == 0:
            visit[s - 1][clip] = 1
            queue.append((s - 1, clip, time + 1))


n = int(input())
visit = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

print(bfs())