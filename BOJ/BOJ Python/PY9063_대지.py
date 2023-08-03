n = int(input())
l, r, b, t = 99999, -99999, 99999, -99999

for i in range(n):
    x, y = map(int, input().split())
    l = min(l, x)
    r = max(r, x)
    b = min(b, y)
    t = max(t, y)

print((r - l) * (t - b))