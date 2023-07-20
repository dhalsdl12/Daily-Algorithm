n = int(input())
arr = list(map(int, input().split())) + [0, 0]
answer = 0

for i in range(n):
    if arr[i + 1] > arr[i + 2]:
        # 첫번째와 두번째를 최대로 구매
        count = min(arr[i], arr[i + 1] - arr[i + 2])
        answer += count * 5
        arr[i] -= count
        arr[i + 1] -= count
        
        # 첫번째, 두번째, 세번째를 최대로 구매
        count = min(arr[i : i + 3])
        answer += count * 7
        arr[i] -= count
        arr[i + 1] -= count
        arr[i + 2] -= count
    
    else:
        # 첫번째, 두번째, 세번째를 최대로 구매
        count = min(arr[i : i + 3])
        answer += count * 7
        arr[i] -= count
        arr[i + 1] -= count
        arr[i + 2] -= count

        # 첫번째와 두번째를 최대로 구매
        count = min(arr[i], arr[i + 1])
        answer += count * 5
        arr[i] -= count
        arr[i + 1] -= count
    
    answer += arr[i] * 3

print(answer)