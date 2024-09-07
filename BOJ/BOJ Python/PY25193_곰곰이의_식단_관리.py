import math

n = int(input())
s = input()
a, b = 0, 0

for c in s:
    if c == 'C':
        a += 1
    else:
        b += 1

print(math.ceil(a / (b + 1)))