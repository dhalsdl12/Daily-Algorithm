num = int(input())
weight = []
height = []
count = []

for i in range(num):
    w, h = map(int, input().split())
    weight.append(w)
    height.append(h)

for i in range(num):
    cnt = 1
    for j in range(num):
        if weight[i] < weight[j] and height[i] < height[j]:
            cnt += 1
    count.append(cnt)

for i in range(num):
    print(count[i], end = " ")