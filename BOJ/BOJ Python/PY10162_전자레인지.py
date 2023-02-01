t = int(input())

# A 5분
# B 1분
# C 10초

a = t // 300
t %= 300
b = t // 60
t %= 60
c = t // 10
t %= 10

if t != 0:
    print(-1)
else:
    print(a, b, c)