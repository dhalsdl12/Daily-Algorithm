import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

max1 = -1000000
min1 = 1000000

for i in range(n):
    if num[i] > max1:
        max1 = num[i]
    
    if num[i] < min1:
        min1 = num[i]

print(min1, max1)