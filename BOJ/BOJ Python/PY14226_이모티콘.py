from collections import deque


def bfs():
    queue = deque()
    queue.append((1, 0, 0))
    visit[1][0] = 1
    while queue:
        inputs, clip, time = queue.popleft()
        if inputs == n:
            return time
        
        tmp = inputs + clip
        if visit[inputs][inputs] == 0:
            visit[inputs][inputs] = 1
            queue.append((inputs, inputs, time + 1))
        if tmp <= n and visit[tmp][clip] == 0:
            visit[tmp][clip] = 1
            queue.append((tmp, clip, time + 1))
        if inputs - 1 >= 0 and visit[inputs - 1][clip] == 0:
            visit[inputs - 1][clip] = 1
            queue.append((inputs - 1, clip, time + 1))


n = int(input())
visit = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

print(bfs())