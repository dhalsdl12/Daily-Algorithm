n = int(input())
arr = []
answer = []
check = 0
min_height = 999993

for i in range(n):
    a, b = map(int, input().split())
    arr.append([a - b, a, b])

arr = sorted(arr, key=lambda x: (-x[0], -x[1]))

for k, a, b in arr:
    check += a
    answer.append(check)
    check -= b
    min_height = min(min_height, check)

print(sum(answer) - min_height * len(answer))