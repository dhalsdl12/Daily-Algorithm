import sys
input = sys.stdin.readline

def init(start, end, index):
    if start > end:
        return
    
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    
    mid = (start + end) // 2
    tree[index] = min(init(start, mid, index * 2), init(mid + 1, end, index * 2 + 1))

    return tree[index]


def update(start, end, index, what, value):
    if what < start or what > end:
        return 1000000000
    
    if start == end:   
        if start == what:
            tree[index] = value
            return value
        else:
            return tree[index]
    
    mid = (start + end) // 2
    if start <= what <= mid:
        tree[index] = min(tree[index * 2 + 1], update(start, mid, index * 2, what, value))
        return tree[index]
    elif mid <= what <= end:
        tree[index] = min(tree[index * 2], update(mid + 1, end, index * 2 + 1, what, value))
        return tree[index]


def get_min(start, end, index, value):
    global result

    if tree[index] == 0 or tree[index] != value or result != 0:
        return
    
    if start == end and tree[index] == value:
        result = start
        return
    
    mid = (start + end) // 2
    get_min(start, mid, index * 2, value)
    get_min(mid + 1, end, index * 2 + 1, value)
    


n = int(input())
answer = []
arr = list(map(int, input().split()))

tree = [0 for _ in range(len(arr) * 4)]
init(0, len(arr) - 1, 1)

m = int(input())

for i in range(m):
    li = list(map(int, input().split()))

    if li[0] == 1:
        update(0, len(arr) - 1, 1, li[1] - 1, li[2])
    else:
        result = 0
        get_min(0, len(arr) - 1, 1, tree[1])
        answer.append(result + 1)

for ans in answer:
    print(ans)