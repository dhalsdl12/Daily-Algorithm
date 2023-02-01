a, b, c = map(int, input().split())
d = int(input())

c += d % 60
d //= 60
if c >= 60:
    b += c // 60
    c %= 60
b += d % 60
if b >= 60:
    a += b // 60
    b %= 60
d //= 60
a += d

print(a % 24, b, c)