n, m, k = map(int, input().split())

fo = m
fx = n - m
bo = k
bx = n - k

print(min(fo, bo) + min(fx, bx))