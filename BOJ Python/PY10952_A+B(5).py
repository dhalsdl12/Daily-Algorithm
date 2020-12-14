import sys

result = []

while(True):
    a, b = map(int, sys.stdin.readline().split())
    if(a == 0 & b == 0):
        break
    else:
        result.append(a+b)

for i in range(len(result)):
    print(result[i])