n = int(input())
tmp = []
for _ in range(n):
    s, e, c = map(int, input().split())
    tmp.append([s, e, c])

tmp.sort()
result = []
check = 0
for i in range(len(tmp)):
    if i == 0:
        result.append(tmp[i])
    else:
        if result[check][0] <= tmp[i][0] <= result[check][1]:
            result[check][1] = max(result[check][1], tmp[i][1])
            result[check][2] = min(result[check][2], tmp[i][2])
        else:
            result.append(tmp[i])
            check += 1
print(len(result))
for res in result:
    for r in res:
        print(r, end=' ')
    print()