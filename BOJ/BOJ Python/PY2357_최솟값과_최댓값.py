import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def init(start, end, index):
    if start == end:
        tree[index] = [arr[start], arr[start]]
        return tree[index]

    mid = (start + end) // 2
    l = init(start, mid, index * 2)
    r = init(mid + 1, end, index * 2 + 1)
    tree[index] = [min(l[0], r[0]), max(l[1], r[1])]

    return tree[index]


def find(start, end, index, left, right):
    if start > right or end < left:
        return [10 ** 9 + 1, 0]
    
    if left <= start and right >= end:
        return tree[index]
    
    mid = (start + end) // 2
    l = find(start, mid, index * 2, left, right)
    r = find(mid + 1, end, index * 2 + 1, left, right)
    return [min(l[0], r[0]), max(l[1], r[1])]
    
    
n, m = map(int, input().split())
arr = []
tree = [0 for _ in range(n * 4)]
answer = []

for _ in range(n):
    arr.append(int(input()))

init(0, n - 1, 1)

for _ in range(m):
    a, b = map(int, input().split())
    answer.append(find(0, n - 1, 1, a - 1, b - 1))

for ans in answer:
    print(*ans)