# A mod B = C
# (A × D) mod B = (C × D) mod B
# (A + D) mod B = (C + D) mod B
from collections import deque


def bfs():
    queue = deque()
    queue.append((1, '1'))
    visit[1] = 1

    while queue:
        remain, number = queue.popleft()
        if remain == 0:
            return number
        if len(number) > 100:
            return 'BRAK'

        if visit[(remain * 10) % n] == 0:
            visit[(remain * 10) % n] = 1
            queue.append(((remain * 10) % n, number + '0'))
        if visit[(remain * 10 + 1) % n] == 0:
            visit[(remain * 10 + 1) % n] = 1
            queue.append(((remain * 10 + 1) % n, number + '1'))

    return 'BRAK'


t = int(input())
answer = []

for _ in range(t):
    n = int(input())
    visit = [0 for _ in range(n + 1)]
    answer.append(bfs())

for ans in answer:
    print(ans)