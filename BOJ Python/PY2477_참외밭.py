n = int(input())

dir = []
length = []
l = 0
h = 0
minus = 0
for i in range(6):
    a, b = map(int, input().split())
    dir.append(a)
    length.append(b)
    if a == 4 or a == 3:
        if h < b:
            h = b
    elif a == 1 or a == 2:
        if l < b:
            l = b
for i in range(1, 6):
    if dir[i] in dir[:i]:
        minus = length[i]*length[i-1]
        break
print(n*(l*h - minus))

