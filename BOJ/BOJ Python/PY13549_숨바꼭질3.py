from collections import deque


def bfs():
    queue = deque()
    queue.append([n, 0])
    visit = [0 for _ in range(100001)]
    visit[n] = 1
    while queue:
        x, cnt = queue.popleft()
        if x == k:
            return cnt
        
        if 0 <= x - 1 <= 100000 and visit[x - 1] == 0:
            queue.append([x - 1, cnt + 1])
            visit[x - 1] = 1
        if 0 <= x * 2 <= 100000 and visit[x * 2] == 0:
            queue.append([x * 2, cnt])
            visit[x * 2] = 1
        if 0 <= x + 1 <= 100000 and visit[x + 1] == 0:
            queue.append([x + 1, cnt + 1])
            visit[x + 1] = 1
    
    return -1


n, k = map(int, input().split())
print(bfs())