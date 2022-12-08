import math


def f(x):
    return a * x + b * math.sin(x) - c


a, b, c = map(int, input().split())
check = 10 ** (-9)
s, e = 0, 2*c

while abs(s - e) > check:
    mid = (s + e) / 2
    if f(mid) == 0:
        break
    elif f(mid) < 0:
        s = mid
    else:
        e = mid

print(mid)