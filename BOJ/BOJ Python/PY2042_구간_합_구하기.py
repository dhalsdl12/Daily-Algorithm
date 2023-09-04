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
    
    if left <= start and right >= end:
        return tree[index]
    
    mid = (start + end) // 2

    l = seg_sum(start, mid, index * 2, left, right)
    r = seg_sum(mid + 1, end, index * 2 + 1, left, right)
    return l + r

n, m, k = map(int, input().split())
arr = []
answer = []
tree = [0 for _ in range(n * 4)]

for i in range(n):
    arr.append(int(input()))
init(0, n - 1, 1)

for i in range(m + k):
    a, b, c = map(int, input().split())

    if a == 1:
        update(0, n - 1, 1, b - 1, c - arr[b - 1])
        arr[b - 1] = c
    elif a == 2:
        answer.append(seg_sum(0, n - 1, 1, b - 1, c - 1))

for ans in answer:
    print(ans)