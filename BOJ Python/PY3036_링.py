def gcd(a, b):
    mod = a%b
    while mod >0:
        a = b
        b = mod
        mod = a%b
    return b

num = int(input())
radius = []
first = []
second = []

radius = list(map(int, input().split()))

for i in range(1,num):
    g = gcd(radius[0], radius[i])
    first.append(radius[0]/g)
    second.append(radius[i]/g)

for i in range(num-1):
    print(int(first[i]),end = "")
    print("/", end = "")
    print(int(second[i]), end = "")
    print()