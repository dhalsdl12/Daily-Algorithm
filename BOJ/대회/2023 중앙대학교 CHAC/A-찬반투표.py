from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

cnt = Counter(arr)
if cnt[0] >= n / 2:
    print('INVALID')
elif cnt[1] > cnt[-1]:
    print('APPROVED')
else:
    print('REJECTED')