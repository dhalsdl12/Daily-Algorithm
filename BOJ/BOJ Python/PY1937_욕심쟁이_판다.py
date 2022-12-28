import sys
sys.setrecursionlimit(10 ** 6)


def dfs(x, y):
    if dp[x][y] != 0:
        return dp[x][y]
    dp[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if li[x][y] < li[nx][ny]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]


n = int(input())

li = []
for i in range(n):
    li.append(list(map(int, input().split())))

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

dp = [[0 for _ in range(n)] for _ in range(n)]
result = 0

for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j))

print(result)
