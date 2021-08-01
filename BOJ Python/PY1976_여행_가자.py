import sys
sys.setrecursionlimit(10**6)


def parents(target):
    if target == parent[target]:
        return target
    #par = parents(parent[target])
    #parent[target] = par
    parent[target] = parents(parent[target])

    return parent[target]


def union(a, b):
    a = parents(a)
    b = parents(b)
    if a == b:
        return
    elif a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

for i in range(1, n + 1):
    l = list(map(int, sys.stdin.readline().split()))

    for j in range(1, len(l) + 1):
        if l[j - 1] == 1:
            union(i, j)

tour = list(map(int, sys.stdin.readline().split()))
result = set([parents(i) for i in tour])

if len(result) != 1:
    print('NO')
else:
    print('YES')
