def gcds(a, b):
    a, b = max(a, b), min(a, b)
    while b != 0:
        a, b = b, a % b
    return a
 
 
n = int(input())
answer = []
for _ in range(n):
    m = int(input())
    Max = 0
    arr = list(map(int, input().split()))
    for i in range(m):
        Max = gcds(Max, arr[i])
    answer.append(arr[m - 1] // Max)
for ans in answer:
    print(ans)