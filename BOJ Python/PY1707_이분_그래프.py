from collections import deque
import sys


def bfs(start):
    visit[start] = 1
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        for m in s[a]:
            if visit[m] == 0:
                visit[m] = -visit[a]
                q.append(m)
            else:
                if visit[m] == visit[a]:
                    return False
    return True


num = int(sys.stdin.readline())
result = []

for i in range(num):
    isTrue = True
    v, e = map(int, sys.stdin.readline().split())
    s = [[] for i in range(v + 1)]
    visit = [0 for _ in range(v+1)]
    for j in range(e):
        a, b = map(int, sys.stdin.readline().split())
        s[a].append(b)
        s[b].append(a)

    for k in range(1, v + 1):
        if visit[k] == 0:
            if not bfs(k):
                isTrue = False
                break
    if isTrue:
        result.append(1)
    else:
        result.append(0)

for i in result:
    if i == 1:
        print("YES")
    elif i == 0:
        print("NO")
