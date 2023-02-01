num = int(input())
tri = []
for i in range(num):
    tri.append(list(map(int, input().split())))

k = 2
for i in range(1, num):
    for j in range(k):
        if j == 0:
            tri[i][j] += tri[i-1][j]
        elif i == j:
            tri[i][j] += tri[i-1][j-1]
        else:
            tri[i][j] += max(tri[i-1][j], tri[i-1][j-1])
    k += 1
print(max(tri[num-1]))