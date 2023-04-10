from collections import deque


def bfs(x):
    queue = deque()
    queue.append((x, 0))
    visit = [-1 for _ in range(n)]
    visit[x] = 0

    while queue:
        x, cnt = queue.popleft()
        for nx in arr[x]:
            if visit[nx] == -1:
                visit[nx] = cnt + 1
                queue.append((nx, cnt + 1))
                
    return sum(visit)
 

n, m = map(int, input().split())
arr = [[] for _ in range(n)]
answer = 99999
idx = -1

for i in range(m):
    a, b = map(int, input().split())
    arr[a - 1].append(b - 1)
    arr[b - 1].append(a - 1)

for i in range(n):
    tmp = bfs(i)
    if answer > tmp:
        idx = i + 1
        answer = tmp

print(idx)