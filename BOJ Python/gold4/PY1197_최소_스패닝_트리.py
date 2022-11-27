# 크루스칼
def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]


v, e = map(int, input().split())
root = [i for i in range(v + 1)]
arr = []
for i in range(e):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[2])
answer = 0

for a, b, c in arr:
    aroot = find(a)
    broot = find(b)

    if aroot != broot:
        if aroot > broot:
            root[aroot] = broot
        elif aroot < broot:
            root[broot] = aroot

        answer += c

print(answer)
