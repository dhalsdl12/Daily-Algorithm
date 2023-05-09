def dfs(d):
    arr[d] = -2
    for i in range(len(arr)):
        if arr[i] == d:
            dfs(i)


n = int(input())
arr = list(map(int, input().split()))
d = int(input())

answer = 0
dfs(d)

for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        answer += 1

print(answer)