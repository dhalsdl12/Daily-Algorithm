import sys


def dfs(idx):
    if idx == len(blank):
        for gra in graph:
            print(*gra)
        exit(0)

    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if row(x, i) and col(y, i) and rect(x, y, i):
            graph[x][y] = i
            dfs(idx+1)
            graph[x][y] = 0


def row(x, a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True


def col(y, a):
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True


def rect(x, y, a):
    x_rect = x // 3 * 3
    y_rect = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == graph[x_rect+i][y_rect+j]:
                return False
    return True


graph = []
blank = []

for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))

dfs(0)
