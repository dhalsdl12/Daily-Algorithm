from collections import deque


def bfs(mid):
    queue = deque()
    queue.append(a)
    visit = [0 for _ in range(n + 1)]
    visit[a] = 1

    while queue:
        x = queue.popleft()

        if x == b:
            return True
                
        for nn, weight in arr[x]:
            if visit[nn] == 0 and mid <= weight:
                visit[nn] = 1
                queue.append(nn)
    
    return False


n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])

a, b = map(int, input().split())
s, e = 1, 1000000000

while s <= e:
    mid = (s + e) // 2

    if bfs(mid):
        s = mid + 1
    else:
        e = mid - 1

print(e)