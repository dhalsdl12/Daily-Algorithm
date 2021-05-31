n, k = map(int, input().split())

item = [[0, 0]]
for i in range(n):
    item.append(list(map(int, input().split())))

bag = [[0]*(k+1) for _ in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= item[i][0]:
            bag[i][j] = max(bag[i-1][j], bag[i-1][j-item[i][0]]+item[i][1])
        else:
            bag[i][j] = bag[i-1][j]

print(bag[n][k])