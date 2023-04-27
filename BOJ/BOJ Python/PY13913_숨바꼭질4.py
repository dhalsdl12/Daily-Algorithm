from collections import deque


def move(x, time, check):
    tmp = x
    li = []
    for _ in range(time + 1):
        li.append(tmp)
        tmp = check[tmp]
    
    return li[::-1]


def bfs():
    queue = deque()
    queue.append((n, 0))
    visit = [0 for _ in range(100001)]
    visit[n] = 1
    check = [0 for _ in range(100001)]

    while queue:
        x, time = queue.popleft()
        if x == k:
            return time, move(x, time, check)
        
        if x + 1 <= 100000 and visit[x + 1] == 0:
            visit[x + 1] = 1
            queue.append((x + 1, time + 1))
            check[x + 1] = x
        
        if x - 1 >= 0 and visit[x - 1] == 0:
            visit[x - 1] = 1
            queue.append((x - 1, time + 1))
            check[x - 1] = x
        
        if x * 2 <= 100000 and visit[x * 2] == 0:
            visit[x * 2] = 1
            queue.append((x * 2, time + 1))
            check[x * 2] = x


n, k = map(int, input().split())

a, b = bfs()
print(a)
print(*b)