n = int(input())
matrix = []
dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    r, c = map(int, input().split())
    matrix.append((r, c))

for i in range(1, n):
    for j in range(0, n - i):
        if i == 1:
            dp[j][j + 1] = matrix[j][0] * matrix[j][1] * matrix[j + 1][1]
            continue

        dp[j][j + i] = 2 ** 31 - 1
        for k in range(j, j + i): 
            dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k + 1][j + i] + matrix[j][0] * matrix[k][1] * matrix[j +i][1])

print(dp[0][-1])