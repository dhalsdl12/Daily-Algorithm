n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

answer = []
dp = [[0 for _ in range(sum(arr) + 1)] for _ in range(n + 1)]
dp[0][0] = 1

for i in range(n):
    for j in range(sum(arr) + 1):
        if dp[i][j] == 1:
            dp[i + 1][j] = 1
            dp[i + 1][j + arr[i]] = 1
            dp[i + 1][abs(j - arr[i])] = 1

for a in arr2:
    if a <= sum(arr) and dp[n][a] == 1:
        answer.append('Y')
    else:
        answer.append('N')
print(*answer)