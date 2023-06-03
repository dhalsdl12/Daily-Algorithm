arr = list(map(int, input().split()))
arr.sort()

a = arr[1] - arr[0]
b = arr[2] - arr[1]

if a == b:
    print(arr[2] + a)
elif a > b:
    print(arr[0] + a // 2)
else:
    print(arr[1] + b // 2)