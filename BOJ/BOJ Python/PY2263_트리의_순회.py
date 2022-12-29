import sys
sys.setrecursionlimit(10 ** 6)


def preorder(inl, inr, postl, postr):
    if inl > inr or postl > postr:
        return

    root = post_order[postr]
    print(root, end = " ")

    left = pos[root] - inl
    right = inr - pos[root]
    preorder(inl, inl + left - 1, postl, postl + left - 1)
    preorder(inr - right + 1, inr, postr - right, postr - 1)



num = int(input())

in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

pos = [0]*(num+1)
for i in range(num):
    pos[in_order[i]] = i;

preorder(0, num-1, 0, num-1)