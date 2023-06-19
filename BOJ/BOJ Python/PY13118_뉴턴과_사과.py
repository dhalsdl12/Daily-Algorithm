arr = list(map(int, input().split()))
x, y, r = map(int, input().split())

if x in arr:
    print(arr.index(x) + 1)
else:
    print(0)