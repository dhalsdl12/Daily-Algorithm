n = int(input())
arr = []

for i in range(n):
    a, b = map(int, input().split())

    if a == 1:
        arr.append(b)
    else:
        if len(arr) == 0:
            continue

        max_arr = arr[-1]
        for k in range(len(arr) - 1, -1, -1):
            if max(max_arr - b, 0) <= arr[k]:
                arr[k] = max(max_arr - b, 0) 
            else:
                break
    
print(sum(arr))