k, n, w = map(int, input().split())
cnt = 0
for i in range(1, w + 1):
    cnt += i

if cnt * k <= n:
    print(0)
else: 
    print(cnt * k - n)