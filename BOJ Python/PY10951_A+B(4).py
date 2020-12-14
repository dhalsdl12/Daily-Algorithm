import sys

result = []

while(True):
    try:
        a, b = map(int, sys.stdin.readline().split())
        result.append(a+b)
    except EOFError:
        break
    
for i in range(len(result)):
    print(result[i])