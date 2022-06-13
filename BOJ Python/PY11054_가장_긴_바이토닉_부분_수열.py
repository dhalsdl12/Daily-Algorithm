n = int(input())

li = list(map(int, input().split()))
reverse_li = li[::-1]

up_dp = [1 for _ in range(n)]
do_dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if li[i] > li[j]:
            up_dp[i] = max(up_dp[j] + 1, up_dp[i])
        if reverse_li[i] > reverse_li[j]:
            do_dp[i] = max(do_dp[j] + 1, do_dp[i])

result = []
re_dp = do_dp[::-1]
for i in range(n):
    result.append(re_dp[i] + up_dp[i])
    
print(max(result) - 1)
