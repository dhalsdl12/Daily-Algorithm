import sys

def gcd(a,b):
    mod = a%b
    while mod >0:
        a = b
        b = mod
        mod = a%b
    return b

n = int(sys.stdin.readline())
m = []
ma = []
for i in range(n):
    m.append(int(sys.stdin.readline()))
m.sort()
for i in range(n-1):
    ma.append(m[i+1] - m[i])

if len(ma) == 1:
    g = ma[0]
elif len(ma) == 2:
    g = gcd(ma[0], ma[1])
else:
    g = ma[0]
    for i in range(1, len(ma)):
        g = gcd(g, ma[i])

for i in range(2, g+1):
    if g%i == 0:
        sys.stdout.write(str(i) + ' ')