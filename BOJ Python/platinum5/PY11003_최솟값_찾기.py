from collections import deque

n, l = map(int, input().split())
arr = list(map(int, input().split()))
result = [0 for _ in range(n)]
check = deque()
for i in range(n):
    while check and check[-1][1] > arr[i]:
        check.pop()
    check.append((i, arr[i]))
    if i >= check[0][0] + l:
        check.popleft()
    result[i] = check[0][1]

for re in result:
    print(re, end=' ')