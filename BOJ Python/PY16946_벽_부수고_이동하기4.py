from collections import deque
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visit[x][y] = 1
    count = 1
    while queue:
        cur_x, cur_y = queue.pop()
        zero[cur_x][cur_y] = group
        for dx, dy in direct:
            nx, ny = cur_x + dx, cur_y + dy
            if 0 <= nx < n and 0 <= ny < m and \
                    visit[nx][ny] == 0 and maps[nx][ny] == 0:
                queue.append([nx, ny])
                visit[nx][ny] = 1
                count += 1
    return count


n, m = map(int, input().split())
maps = []
visit = [[0 for _ in range(m)] for _ in range(n)]
zero = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    maps.append(list(map(int, input().rstrip())))

group = 1
group_z = {}
for i in range(n):
    for j in range(m):
        if maps[i][j] == 0 and visit[i][j] == 0:
            group_z[group] = bfs(i, j)
            group += 1
result = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        cnt = 1
        if maps[i][j] == 0:
            continue
        position_4 = set()
        for dx, dy in direct:
            nx, ny = i + dx, j + dy
            if 0 <= nx < n and 0 <= ny < m and \
                    maps[nx][ny] == 0:
                position_4.add(zero[nx][ny])
        for k in position_4:
            cnt += group_z[k]
            cnt %= 10
        result[i][j] = cnt
for re in result:
    for r in re:
        print(r, end='')
    print()
