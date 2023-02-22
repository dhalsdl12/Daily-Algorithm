from collections import deque


def bfs():
    queue = deque()
    queue.append([0, 0])
    visit[0][0] = 1
    count = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
                if arr[nx][ny] == 0:
                    queue.append([nx, ny])
                    visit[nx][ny] = 1
                elif arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    visit[nx][ny] = 1
                    count += 1
    return count


n, m = map(int, input().split())
arr = []
answer = []
time = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    arr.append(list(map(int, input().split())))

while True:
    time += 1
    visit = [[0 for _ in range(m)] for _ in range(n)]
    count = bfs()
    if count == 0:
        break
    answer.append(count)

print(time - 1)
print(answer[-1])