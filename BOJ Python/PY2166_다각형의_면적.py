num = int(input())
a = []
for i in range(num):
    a.append(list(map(int, input().split())))
a.append(a[0])
left = 0
right = 0

for i in range(num):
    left += a[i][0]*a[i+1][1]
    right += a[i][1]*a[i+1][0]

print('%.1f' % float(abs(left-right)/2))
