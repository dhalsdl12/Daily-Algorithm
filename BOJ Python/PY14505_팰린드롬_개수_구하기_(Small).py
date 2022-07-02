s = input()
dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]

for i in range(len(s)):
    dp[i][i] = 1

    if i != len(s) - 1:
        if s[i] == s[i + 1]:
            dp[i][i + 1] = 3
        else:
            dp[i][i + 1] = 2
for i in range(2, len(s)): #길이
    for left in range(len(s)):
        right = left + i

        if right >= len(s):
            break
            
        dp[left][right] = dp[left + 1][right] + dp[left][right - 1] - dp[left + 1][right - 1]
        if s[left] == s[right]:
            dp[left][right] += dp[left + 1][right - 1] + 1

print(dp[0][len(s) - 1])
