n = int(input())
arr = list(map(int, input().split()))

dp = [[0 for _ in range(n)] for _ in range(2)]
dp[0][0] = arr[0]

if n == 1:
    print(dp[0][0])
else:
    answer = -9999999
    for i in range(1, n):
        dp[0][i] = max(dp[0][i - 1] + arr[i], arr[i])
        dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + arr[i])
        answer = max(answer, dp[0][i], dp[1][i])
    print(answer)