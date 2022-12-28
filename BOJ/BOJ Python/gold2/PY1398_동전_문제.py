t = int(input())
coin = [1, 10, 25]
result = []
for i in range(t):
    c = int(input())
    dp = [10 ** 15 + 1 for _ in range(100)]
    dp[0] = 0

    for co in coin:
        for j in range(co, 100):
            dp[j] = min(dp[j], dp[j-co] + 1)

    answer = 0
    while True:
        answer += dp[c % 100]
        c //= 100
        if c == 0:
            result.append(answer)
            break

for re in result:
    print(re)
