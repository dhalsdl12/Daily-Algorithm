def diff(m, n):
    if m == n:
        return 0
    else:
        return 1


a = input()
b = input()
la = len(a)
lb = len(b)
dp = [[0 for _ in range(lb + 1)]for _ in range(la + 1)]
for i in range(1, la + 1):
    dp[i][0] = i
for j in range(1, lb + 1):
    dp[0][j] = j

for i in range(1, la + 1):
    for j in range(1, lb + 1):
        dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1,
                       dp[i - 1][j - 1] + diff(a[i - 1], b[j - 1]))

result = []
while True:
    if la == 0 and lb == 0:
        break
    position = min(dp[la - 1][lb - 1], dp[la][lb - 1], dp[la - 1][lb])
    if position == dp[la][lb]:
        result.append("c " + b[lb - 1])
        la -= 1
        lb -= 1
    elif position == dp[la - 1][lb]:
        result.append("d " + a[la - 1])
        la -= 1
    elif position == dp[la][lb - 1]:
        result.append("a " + b[lb - 1])
        lb -= 1
    elif position == dp[la - 1][lb - 1]:
        result.append("m " + a[la - 1])
        la -= 1
        lb -= 1

for re in result[::-1]:
    print(re)
