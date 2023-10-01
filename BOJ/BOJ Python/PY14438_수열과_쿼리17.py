import sys
input = sys.stdin.readline


def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    
    mid = (start + end) // 2
    l = init(start, mid, index * 2)
    r = init(mid + 1, end, index * 2 + 1)
    tree[index] = min(l, r)
    
    return tree[index]


def update(start, end, index, what, value):
    if start > what or end < what:
        return
    
    if start == end:
        tree[index] = value
        return
    
    mid = (start + end) // 2
    update(start, mid, index * 2, what, value)
    update(mid + 1, end, index * 2 + 1, what, value)
    tree[index] = min(tree[index * 2], tree[index * 2 + 1])


def find(start, end, index, left, right):
    if end < left or start > right:
        return 1000000000
    
    if start >= left and end <= right:
        return tree[index]
    
    mid = (start + end) // 2
    l = find(start, mid, index * 2, left, right)
    r = find(mid + 1, end, index * 2 + 1, left, right)
    return min(l, r)


n = int(input())
arr = list(map(int, input().split()))
answer = []
tree = [0 for _ in range(n * 4)]

init(0, n - 1, 1)

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a == 1:
        arr[b - 1] = c
        update(0, n - 1, 1, b - 1, c)
    elif a == 2:
        answer.append(find(0, n - 1, 1, b - 1, c - 1))

for ans in answer:
    print(ans)