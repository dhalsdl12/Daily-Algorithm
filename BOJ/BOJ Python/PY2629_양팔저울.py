def check(cnt, left, right):
    gap = abs(left - right)
    if gap not in result:
        result.append(gap)
    if cnt == n:
        return 0
    if dp[cnt][gap] == 0:
        check(cnt + 1, left + arr[cnt], right)
        check(cnt + 1, left, right + arr[cnt])
        check(cnt + 1, left, right)

        dp[cnt][gap] = 1


n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

result = []
dp = [[0 for _ in range(15001)] for _ in range(n + 1)]
check(0, 0, 0)

print(dp)