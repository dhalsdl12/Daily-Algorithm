n = int(input())
arr = list(map(int, input().split()))
s = int(input())

for i in range(n):
    num = max(arr[i : min(n, i + s + 1)])
    idx = arr.index(num)

    arr.pop(idx)
    arr.insert(i, num)
    
    s -= (idx - i)
    if s == 0:
        break

print(*arr)