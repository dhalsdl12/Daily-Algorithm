n, m = map(int, input().split())
arr = []
ball = [0 for _ in range(n)]
for _ in range(m): 
    i, j, k = map(int, input().split())

    for b in range(i, j + 1):
        ball[b - 1] = k

print(*ball)