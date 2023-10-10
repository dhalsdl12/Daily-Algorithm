import sys
input = sys.stdin.readline


def update(start, end, index, what, value):
    if what < start or what > end:
        return
    
    if start == end:
        tree[index] = value
    else:
        mid = (start + end) // 2
        update(start, mid, index * 2, what, value)
        update(mid + 1, end, index * 2 + 1, what, value)
        tree[index] = tree[index * 2] + tree[index * 2 + 1]


def find(start, end, index, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[index]
    
    mid = (start + end) // 2
    l = find(start, mid, index * 2, left, right)
    r = find(mid + 1, end, index * 2 + 1, left, right)

    return l + r


n, m = map(int, input().split())
arr = [0 for _ in range(n)]
tree = [0 for _ in range(n * 4)]
answer = []

for i in range(m):
    a, b, c = map(int, input().split())

    if a == 0:
        if b > c:
            b, c = c, b
        answer.append(find(0, n - 1, 1, b - 1, c - 1))
    elif a == 1:
        update(0, n - 1, 1, b - 1, c)
        arr[b - 1] = c

for ans in answer:
    print(ans)