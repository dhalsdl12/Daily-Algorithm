n = int(input())
arr = list(map(int, input().split()))

answer = 0

for i in range(n):
    tmp = n - i
    answer = max(answer, arr[i] - tmp)

print(answer)
