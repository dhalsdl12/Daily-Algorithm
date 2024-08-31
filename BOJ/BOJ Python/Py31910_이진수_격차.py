n = int(input())
arr = []
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    arr.append(list(map(int, input().split())))

dp[0][0] = arr[0][0]

for i in range(1, n):
    dp[0][i] = dp[0][i - 1] * 2 + arr[0][i]

for j in range(1, n):
    dp[j][0] = dp[j - 1][0] * 2 + arr[j][0]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) * 2 + arr[i][j]
    
print(dp[-1][-1])