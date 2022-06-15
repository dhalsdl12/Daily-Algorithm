def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]


n = int(input())

li = []
dist_li = []
root = list(range(n))
edge, cost = 0, 0

for i in range(n):
    x, y, z = list(map(int, input().split()))
    li.append([x, y, z, i])

for j in range(3):
    li = sorted(li, key=lambda x: x[j])
    bf_location = li[0][3]
    for i in range(1, n):  # 각 좌표별로 간선추가
        cur_location = li[i][3]
        dist_li.append([abs(li[i][j] - li[i - 1][j]), bf_location, cur_location])
        bf_location = cur_location

dist_li = sorted(dist_li, key=lambda x: x[0])
for point, s, f in dist_li:
    a, b = find(s), find(f)
    if a != b:
        root[b] = a
        edge += 1
        cost += point
    if edge == n - 1:
        break

print(cost)
