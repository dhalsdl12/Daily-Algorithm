n, m = map(int, input().split())
arr = [i + 1 for i in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    tmp = arr[i - 1]
    arr[i - 1] = arr[j - 1]
    arr[j - 1] = tmp

print(*arr)