n, m = map(int, input().split())
answer = []
arr = list(map(int, input().split()))

Sum = [0]
for i in range(len(arr)):
    Sum.append(Sum[i] + arr[i])

for i in range(m):
    x, y = map(int, input().split())
    answer.append(Sum[y] - Sum[x - 1])

for ans in answer:
    print(ans)