from collections import deque

def bfs():
    while queue:
        v = queue.popleft()

        for i in arr[v]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                queue.append(i)

n, m, r = map(int, input().split())
arr = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
visited[r] = 1
cnt = 1

queue = deque([r])

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, n + 1):
    arr[i].sort(reverse=True)

while queue:
    v = queue.popleft()

    for i in arr[v]:
        if visited[i] == 0:
            cnt += 1
            visited[i] = cnt
            queue.append(i)

for v in visited[1:]:
    print(v)