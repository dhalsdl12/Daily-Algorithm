from collections import deque


def bfs():
    queue = deque()
    queue.append((a, 0))
    visit[a] = 1

    while queue:
        x, cnt = queue.popleft()
        if x == b:
            return cnt
        
        for i in range(len(arr[x])):
            nx = arr[x][i]
            if visit[nx] == 0:
                visit[nx] = 1
                queue.append((nx, cnt + 1))

    return -1


n = int(input())
arr = [[] for _ in range(n + 1)]
visit = [0 for _ in range(n + 1)]

a, b = map(int, input().split())
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

print(bfs())