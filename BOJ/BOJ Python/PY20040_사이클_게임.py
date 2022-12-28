import sys
sys.setrecursionlimit(200000)


def find(x):
    if parent[x] != x:
        y = find(parent[x])
        return y
    return x


def union(a, b):
    a = find(a)
    b = find( b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print(i+1)
        break
    union(a, b)
else:
    print(0)
