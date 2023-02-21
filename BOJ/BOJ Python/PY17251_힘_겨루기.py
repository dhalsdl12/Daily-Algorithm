n = int(input())
arr = list(map(int, input().split()))

Max, first, last = 0, 0, 0
for i in range(n):
    if arr[i] > Max:
        Max = arr[i]
        first = i
        last = i
    elif arr[i] == Max:
        last = i

if first > n - 1 - last:
    print('B')
elif first < n - 1 - last:
    print('R')
else:
    print('X')
