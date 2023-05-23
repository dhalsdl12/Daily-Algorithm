arr = []

for _ in range(7):
    n = int(input())
    if n % 2 == 1:
        arr.append(n)

if len(arr) == 0:
    print(-1)
else:
    arr.sort()
    print(sum(arr))
    print(arr[0])