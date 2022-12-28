import sys
from collections import deque

num = int(sys.stdin.readline())
result = []
for i in range(num):
    order = input()
    n = int(sys.stdin.readline())
    number = input()[1:-1].split(',')
    r, f, b = 0,0,0
    for s in order:
        if s == 'R':
            r += 1
        elif s == 'D':
            if r % 2 == 0:
                f += 1
            else:
                b += 1
    if f+b <= n:
        number = number[f:n-b]
        if r%2 == 0:
            print('['+','.join(number)+']')
        else:
            print('['+','.join(number[::-1])+']')
    else:
        print('error')