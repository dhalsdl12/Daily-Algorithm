import sys

a, b = map(int,sys.stdin.readline().split())

num = list(map(int, sys.stdin.readline().split()))

for i in range(a):
    if num[i] < b:
        print(num[i], end=' ')

