def binary(arr, target, start, end):
    while start <= end:
        mid = (start + end)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


n = int(input())
sang = list(map(int, input().split()))
sang.sort()
m = int(input())
card = list(map(int, input().split()))
result = []

for i in range(m):
    if binary(sang, card[i], 0, n-1) != -1:
        result.append(1)
    else:
        result.append(0)

for i in result:
    print(i, end=" ")