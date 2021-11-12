def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c]:
        return dp[a][b][c]
    if a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]


dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
arr = []
result = []
while True:
    arr.append(list(map(int, input().split())))

    if arr[-1][0] == -1 and arr[-1][1] == -1 and arr[-1][2] == -1:
        arr.pop()
        break
    result.append(w(arr[-1][0], arr[-1][1], arr[-1][2]))

for i in range(len(arr)):
    print("w(%d, %d, %d) = %d" %(arr[i][0], arr[i][1], arr[i][2], result[i]))
