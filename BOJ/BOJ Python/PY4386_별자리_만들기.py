import math
import heapq

n = int(input())
star = []
G = [[]for _ in range(n)]
for i in range(n):
    x, y = map(float, input().split())
    star.append([x,y])

for i in range(n-1):
    for j in range(i, n):
        dis = round(math.sqrt((star[i][0]-star[j][0])**2 +
                              (star[i][1]-star[j][1])**2), 2)
        if i == j:
            continue
        G[i].append([dis, j])
        G[j].append([dis, i])

q = []
heapq.heappush(q, [0, 0])

mst_val = 0
check = [0 for _ in range(n)]

while q:
    dis, end = heapq.heappop(q)
    if check[end] == 1:
        continue
    mst_val += dis
    check[end] = 1
    for dis, end in G[end]:
        heapq.heappush(q, [dis, end])

print(mst_val)