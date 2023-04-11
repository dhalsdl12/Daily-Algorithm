from collections import deque


def bfs():
    queue = deque()
    queue.append((a, ''))
    visit = [0 for _ in range(10000)]
    visit[a] = 1

    while queue:
        tmp, string = queue.popleft()
        if tmp == b:
            return string
        
        
        tmp2 = (tmp * 2) % 10000
        if visit[tmp2] == 0:
            visit[tmp2] = 1
            queue.append((tmp2, string + 'D'))

        tmp2 = (tmp - 1) % 10000
        if visit[tmp2] == 0:
            visit[tmp2] = 1
            queue.append((tmp2, string + 'S'))

        tmp2 = tmp // 1000 + (tmp % 1000) * 10
        if visit[tmp2] == 0:
            visit[tmp2] = 1
            queue.append((tmp2, string + 'L'))

        tmp2 = (tmp % 10) * 1000 + tmp // 10
        if visit[tmp2] == 0:
            visit[tmp2] = 1
            queue.append((tmp2, string + 'R'))


t = int(input())
answer = []

for _ in range(t):
    a, b = map(int, input().split())
    answer.append(bfs())

for ans in answer:
    print(ans)