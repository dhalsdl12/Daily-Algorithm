import sys
def binary(l, num1, start, end):
    if start > end:
        return 0
    mid = (start+end) // 2
    if(l == num1[mid]):
        return 1
    elif l < num1[mid]:
        return binary(l, num1, start, mid-1)
    else:
        return binary(l, num1, mid+1, end)  

n = int(sys.stdin.readline())
num1 = sorted(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
num2 = map(int, sys.stdin.readline().split())

for l in num2:
    start = 0
    end = len(num1)-1
    print(binary(l, num1, start, end))