m = int(input())

arr = [1,2,3]
for _ in range(m):
    x, y = map(int, input().split())
    
    a = arr.index(x)
    b = arr.index(y)
    
    arr[a], arr[b] = arr[b], arr[a]
    
print(arr[0])