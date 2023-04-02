n = int(input())
arr = []
for _ in range(n):
    c = int(input())
    q = c // 25
    c %= 25
    d = c // 10
    c %= 10
    n = c // 5
    c %= 5
    p = c

    arr.append([q, d, n, p])

for a in arr:
    print(*a)