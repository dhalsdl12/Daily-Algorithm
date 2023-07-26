h, w = map(int, input().split())
arr = [[0 for _ in range(h)] for _ in range(w)]
height = list(map(int, input().split()))
answer = 0

for i in range(w):
    n = height[i]
    for j in range(n):
        arr[i][j] = 1

for j in range(h):
    check = 0
    cnt = 0
    for i in range(w):
        if arr[i][j] == 1:
            if check == 1:
                answer += cnt
                cnt = 0
            check = 1
        else:
            if check == 1:
                cnt += 1

print(answer)