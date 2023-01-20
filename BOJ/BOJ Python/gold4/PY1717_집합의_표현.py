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


n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n+1)]

for i in range(m):
    c, a, b = map(int, sys.stdin.readline().split())
    if c == 0:
        union(a, b)
        #for i in range(n+1):
        #    print(parent[i], end=" ")
    elif c == 1:
        if parents(a) == parents(b):
            print("YES")
        else:
            print("NO")