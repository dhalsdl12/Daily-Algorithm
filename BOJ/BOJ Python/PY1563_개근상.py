import sys
sys.setrecursionlimit(10 ** 6)


def dfs(d, l, a):
    if l == 2 or a == 3:
        return 0
    if d == n:
        return 1
    if dp[d][l][a] == -1:
        dp[d][l][a] = (dfs(d + 1, l, 0)
                       + dfs(d + 1, l + 1, 0)
                       + dfs(d + 1, l, a + 1))
    return dp[d][l][a]


n = int(input())
dp = [[[-1 for _ in range(3)]for _ in range(2)]for _ in range(n)]

print(dfs(0, 0, 0) % 1000000)
