from itertools import product


n, m = map(int, input().split())
arr = []
answer = 0

for _ in range(2):
    a, b, c = map(int, input().split())
    arr.append(a)
    arr.append(b)
    arr.append(c)

for i in product(arr, repeat = n):
    if sum(i) >= m:
        answer += 1

print(answer)