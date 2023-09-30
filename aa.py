import sys
input = sys.stdin.readline


def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    
    mid = (start + end) // 2
    tree[index] = min(init(start, mid, index * 2), init(mid + 1, end, index * 2 + 1))
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
    if start > right or end < left:
        return [1000000000, 1000000000] 
    
    if start >= left and end <= right:
        return tree[index]
    
    mid = (start + end) // 2
    return min(find(start, mid, index * 2, left, right),
               find(mid + 1, end, index * 2 + 1, left, right))


n = int(input())
tmp = list(map(int, input().split()))
arr, answer = [], []
for i in range(n):
    arr.append([tmp[i], i + 1])

tree = [0 for _ in range(n * 4)]
m = int(input())

init(0, n - 1, 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        arr[b - 1][0] = c
        update(0, n - 1, 1, b - 1, arr[b - 1])
    elif a == 2:
        answer.append(find(0, n - 1, 1, b - 1, c - 1)[1])
    
for ans in answer:
    print(ans)