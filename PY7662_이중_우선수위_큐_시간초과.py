import sys

num = int(sys.stdin.readline())
for i in range(num):
    cnt = 0
    heap = []
    n = int(sys.stdin.readline())
    for j in range(n):
        s, number = sys.stdin.readline().split(' ')
        a = int(number)
        if s == "I":
            heap.append(a)
            heap = sorted(heap)
        elif s == "D":
            if a == -1:
                if len(heap)-cnt == 0:
                    continue
                cnt += 1
            elif a == 1:
                if len(heap)-cnt == 0:
                    continue
                heap.pop()
    if len(heap)-cnt == 0:
        print("EMPTY")
    else:
        print(heap.pop(), end=' ')
        if len(heap) == 0:
            continue
        print(heap[cnt])
