import sys
input = sys.stdin.readline


def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    
    mid = (start + end) // 2
    l = init(start, mid, index * 2)
    r = init(mid + 1, end, index * 2 + 1)
    tree[index] = l + r

    return tree[index]


def update(start, end, index, what, value):
    if what < start or what > end:
        return
    
    tree[index] += value
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, index * 2, what, value)
    update(mid + 1, end, index * 2 + 1, what, value)


def seg_sum(start, end, index, left, right):
    if left > end or right < start:
        return 0
    
    if left <= start and end <= right:
        return tree[index]
    
    mid = (start + end) // 2
    l = seg_sum(start, mid, index * 2, left, right)
    r = seg_sum(mid + 1, end, index * 2 + 1, left, right)
    return l + r


n, q = map(int, input().split())

answer = []
tree = [0 for _ in range(n * 4)]
arr = list(map(int, input().split()))

init(0, n - 1, 1)
for _ in range(q):
    x, y, a, b = map(int, input().split())
    if x <= y:
        answer.append(seg_sum(0, n - 1, 1, x - 1, y - 1))
    else:
        answer.append(seg_sum(0, n - 1, 1, y - 1, x - 1))
    update(0, n - 1, 1, a - 1, b - arr[a - 1])
    arr[a - 1] = b

for ans in answer:
    print(ans)