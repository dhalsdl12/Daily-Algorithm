import sys
input = sys.stdin.readline


def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    
    mid = (start + end) // 2
    tree[index] = init(start, mid, index * 2) * init(mid + 1, end, index * 2 + 1) % 1000000007
    return tree[index]

def update(start, end, index, what, value):
    if what < start or what > end:
        return
    
    if start == end:
        tree[index] = value
    else:
        mid = (start + end) // 2
        update(start, mid, index * 2, what, value)
        update(mid + 1, end, index * 2 + 1, what, value)

        tree[index] = tree[index * 2] * tree[index * 2 + 1] % 1000000007


def multi(start, end, index, left, right):
    if start > right or end < left:
        return 1

    if left <= start and right >= end:
        return tree[index]
    
    mid = (start + end) // 2
    return multi(start, mid, index * 2, left, right) * multi(mid + 1, end, index * 2 + 1, left, right) % 1000000007


n, m, k = map(int, input().split())
arr = []
answer = []
tree = [0 for _ in range(n * 4)]

for _ in range(n):
    arr.append(int(input()))

init(0, n - 1, 1)
for i in range(m + k):
    a, b, c = map(int, input().split())
    
    if a == 1:
        update(0, n - 1, 1, b - 1, c)
        arr[b - 1] = c

    if a == 2:
        answer.append(multi(0, n - 1, 1, b - 1, c - 1))
for ans in answer:
    print(ans)