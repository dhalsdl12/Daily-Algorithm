n = int(input())
arr = []
same = [[0 for _ in range(n)] for _ in range(n)]
max_cnt = -1
answer = 0

for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(5):
    tmp = []

    for j in range(n):
        tmp.append(arr[j][i])
    
    for j in range(n):
        cnt = 0
        for k in range(n):
            if j == k:
                continue
            if tmp[j] == tmp[k]:
                same[j][k] = 1

for i in range(n):
    cnt = 0
    for j in range(n):
        if same[i][j] == 1:
            cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt
        answer = i + 1

print(answer)