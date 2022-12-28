a = 0
h = 0
for i in range(2):
    t, f, s, p, c = map(int, input().split())
    if i == 0:  
        a = t * 6 + f * 3 + s * 2 + p * 1 + c * 2
    else:
        h = t * 6 + f * 3 + s * 2 + p * 1 + c * 2

print(a, h)