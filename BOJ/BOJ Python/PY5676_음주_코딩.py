# https://www.acmicpc.net/problem/5676
import sys
input = sys.stdin.readline


def pmz(num):
    if num>0:return 1
    elif num<0:return -1
    else: return 0


def init(start, end, index):
    if start == end:
        arr[start] = pmz(arr[start])
        tree[index] = arr[start]
        return tree[index]

    mid = (start + end) // 2
    l = init(start, mid, index * 2)
    r = init(mid + 1, end, index * 2 + 1)
    tree[index] = l * r

    return tree[index]


def update(start, end, index, what, value):
    if what > end or what < start:
        return
    if start == end:
        tree[index] = value
    else:
        mid = (start + end) // 2
        update(start, mid, index * 2, what, value)
        update(mid + 1, end, index * 2 + 1, what, value)
        tree[index] = tree[index * 2] * tree[index * 2 + 1]


def find(start, end, index, left, right):
    if left > end or start > right:
        return 1
    if left <= start and end <= right:
        return tree[index]
    
    mid = (start + end) // 2
    l = find(start, mid, index * 2, left, right)
    r = find(mid + 1, end, index * 2 + 1, left, right)
    return l * r


result = []
while True:
    try:
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        tree = [0 for _ in range(n * 4)]
        answer = ''

        init(0, n - 1, 1)

        for _ in range(k):
            li = list(input().split())

            if li[0] == 'C':
                a = int(li[1])
                b = int(li[2])
                update(0, n - 1, 1, a - 1, pmz(b))
                arr[a - 1] = pmz(b)

            elif li[0] == 'P':
                a = int(li[1])
                b = int(li[2])
                check = find(0, n - 1, 1, a - 1, b - 1)
                if check == 0:
                    answer += '0'
                elif check > 0:
                    answer += '+'
                else:
                    answer += '-'

        result.append(answer)
    except:
        break
for res in result:
    print(res)
