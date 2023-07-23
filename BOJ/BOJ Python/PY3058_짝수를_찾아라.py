n = int(input())
answer = []

for _ in range(n):
    arr = list(map(int, input().split()))
    Min = 101
    Sum = 0
    for i in range(7):
        if arr[i] % 2 == 0:
            Sum += arr[i]
            Min = min(Min, arr[i])
    
    answer.append((Sum, Min))

for S, M in answer:
    print(S, M)