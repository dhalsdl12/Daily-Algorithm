n = int(input())
arr = list(map(int, input().split()))

sum = 0
answer = 0

for i in range(n):
    if arr[i] == 1:
        sum += 1
        answer += sum
    else:
        sum = 0

print(answer)