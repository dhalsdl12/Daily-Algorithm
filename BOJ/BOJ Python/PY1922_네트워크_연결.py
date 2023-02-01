def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
m = int(input())

answer = 0
edge = []
parent = [i for i in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))

edge.sort()

for e in edge:
    c, a, b = e
    if find(a) != find(b):
        union(a, b)
        answer += c

print(answer)