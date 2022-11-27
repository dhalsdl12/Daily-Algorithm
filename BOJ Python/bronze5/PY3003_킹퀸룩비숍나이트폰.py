a = list(map(int, input().split()))
b = [1, 1, 2, 2, 2, 8]
result = []
for i in range(6):
    result.append(b[i] - a[i])

for re in result:
    print(re, end=' ')
