#18436 수열과 쿼리 37

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def init(start, end, index):
    if start == end:
        if arr[start] % 2 == 0:
            tree[index][0] = 1
        else:
            tree[index][1] = 1

        return tree[index]

    mid = (start + end) // 2

    init(start, mid, index * 2)
    init(mid + 1, end, index * 2 + 1)

    tree[index] = [tree[index * 2][0] + tree[index * 2 + 1][0], tree[index * 2][1] + tree[index * 2 + 1][1]]
    
    return tree[index]


def update(start, end, index, what, value):
    if what < start or what > end:
        return
    
    if start == end:
        if value % 2 == 0:
            tree[index] = [1, 0]
        else:
            tree[index] = [0, 1]
        return tree[index]
    else:
        mid = (start + end) // 2

        update(start, mid, index * 2, what, value)
        update(mid + 1, end, index * 2 + 1, what, value)

        tree[index] = [tree[index * 2][0] + tree[index * 2 + 1][0], tree[index * 2][1] + tree[index * 2 + 1][1]]

def even_odd(start, end, index, left, right):
    if start > right or end < left:
        return [0, 0]
    
    if left <= right and right >= end:
        return tree[index]
    
    mid = (start + end) // 2
    left_a = even_odd(start, mid, index * 2, left, right)
    right_a = even_odd(mid + 1, end, index * 2 + 1, left, right)

    return [left_a[0] + right_a[0], left_a[1] + right_a[1]]

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

tree = [[0, 0] for _ in range(n * 4)]
answer = []

for i in range(m):
    a, b, c = map(int, input().split())

    if a == 1:
        if arr[b - 1] % 2 == c % 2:
            arr[b - 1] = c
            continue
        else:
            update(0, n - 1, 1, b - 1, c)
            arr[b - 1] = c
    elif a == 2:
        answer.append(even_odd(0, n - 1, 1, b - 1, c - 1)[0])
    elif a == 3:
        answer.append(even_odd(0, n - 1, 1, b - 1, c - 1)[1])

for ans in answer:
    print(ans)