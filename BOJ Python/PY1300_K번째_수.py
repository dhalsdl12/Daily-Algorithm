import sys


n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

low = 1
high = k
ans = 0

while low <= high:
    mid = (low + high)//2
    count = 0

    for i in range(1, n+1):
        count = count + min(mid//i, n)

    if count < k:
        low = mid + 1
    else:
        ans = mid
        high = mid - 1

print(ans)