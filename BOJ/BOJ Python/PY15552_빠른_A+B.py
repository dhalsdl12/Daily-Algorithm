import sys

num = int(sys.stdin.readline())
result = []

for i in range(num):
    a, b = map(int, sys.stdin.readline().split())
    result.append(a+b)

for i in range(len(result)):
    print(result[i]) 
