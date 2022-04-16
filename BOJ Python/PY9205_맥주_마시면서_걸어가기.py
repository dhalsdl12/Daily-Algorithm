from collections import deque


def bfs():
    q = deque()
    q.append([home[0], home[1]])
    while q:
        x, y = q.popleft()
        if abs(x - fest[0]) + abs(y - fest[1]) <= 1000:
            return "happy"
        for i in range(n):
            if not visited[i]:
                new_x, new_y = conv[i]
                if abs(x - new_x) + abs(y - new_y) <= 1000:
                    q.append([new_x, new_y])
                    visited[i] = 1
    return "sad"


t = int(input())
result = []
for i in range(t):
    n = int(input())
    x, y = map(int, input().split())
    home = [x, y]
    conv = []
    for j in range(n):
        x, y = map(int, input().split())
        conv.append([x, y])
    x, y = map(int, input().split())
    fest = [x, y]
    visited = [0 for i in range(n+1)]
    result.append(bfs())

for re in result:
    print(re)
