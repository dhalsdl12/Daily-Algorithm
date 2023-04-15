n = int(input())

money = list(map(int, input().split()))
y = 0
m = 0

for i in range(n):
    yy = money[i] // 30
    mm = money[i] // 60

    y += (10 * (yy + 1))
    m += (15 * (mm + 1))

if y > m:
    print('M ' + str(m))
elif y < m:
    print('Y ' + str(y))
else:
    print('Y M ' + str(y))