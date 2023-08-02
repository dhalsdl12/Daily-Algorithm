n = int(input())
arr = sorted(map(int, input().split()))
print(arr)
print()
if sum(arr) != n * (n - 1) // 2:
    print(-1)
    exit()

for i in range(n):
    win = arr[i]
    loss = n - arr[i] - 1 - i

    for j in range(n - loss, n):
        arr[j] -= 1
        if arr[j] < 0:
            print(-1)
            exit()
        
    arr[i] = 0
    print(arr)
    arr.sort()
    print(arr)
    print()
print(1)