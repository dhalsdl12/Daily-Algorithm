from collections import deque


def bfs():
    queue = deque()
    queue.append((puzzle, 0))

    visit = {}
    visit[puzzle] = 0

    while queue:
        now, cnt = queue.popleft()

        if now == '123456780':
            return cnt
        
        p = now.find('0')
        x = p // 3
        y = p % 3

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 3 and 0 <= ny < 3:
                np = nx * 3 + ny
                nn = list(now)
                nn[np], nn[p] = nn[p], nn[np]
                nn = ''.join(nn)

                if nn not in visit:
                    queue.append((nn, cnt + 1))
                    visit[nn] = 0
    return -1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
puzzle = ''
for _ in range(3):
    tmp = input().strip()
    tmp = tmp.replace(' ', '')
    puzzle += tmp

print(bfs())