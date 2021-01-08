import sys

n = int(sys.stdin.readline())

lst = [0 for i in range(10000)]

for i in range(n):
    x = int(sys.stdin.readline())
    lst[x-1] += 1

for idx, cnt in enumerate(lst):
    if cnt != 0:
        for i in range(cnt):
            sys.stdout.write('{}\n'.format(idx+1))