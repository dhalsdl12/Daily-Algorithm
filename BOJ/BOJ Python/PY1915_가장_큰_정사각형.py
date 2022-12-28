n, m = map(int, input().split())

arr = []
for i in range(n):
    a = []
    b = int(input())
    for j in range(m):
        a.append(b // (10 ** (m - j - 1)))
        b %= (10 ** (m - j - 1))
    arr.append(a)

dp = [[0 for _ in range(m)] for _ in range(n)]
Max = 0
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = arr[i][j]
        elif arr[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
        if Max < dp[i][j]:
            Max = dp[i][j]

print(Max ** 2)
