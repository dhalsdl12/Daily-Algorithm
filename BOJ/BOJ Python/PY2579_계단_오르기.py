n = int(input())
check = 0
stair = []
dp = [0 for i in range(301)]
for i in range(n):
    stair.append(int(input()))

dp[0] = stair[0]
if n >= 2:
    dp[1] = stair[0] + stair[1]

if n > 3:
    dp[2] = max(stair[0] + stair[1], stair[0] + stair[2])
elif n == 3:
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

for i in range(3, n):
    if i == n-2:
        if dp[i - 2] + stair[i] >= dp[i - 3] + stair[i - 1] + stair[i]:
            dp[i] = dp[i - 2] + stair[i]
            check = 1
        else:
            dp[i] = dp[i - 3] + stair[i - 1] + stair[i]
            check = 2
    elif i == n-1:
        if check == 1:
            dp[i] = dp[i-1] + stair[i]
        elif check == 2:
            dp[i] = dp[i-2] + stair[i]


    else:
        dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])

print(dp[n-1])

