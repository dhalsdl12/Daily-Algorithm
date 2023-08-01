t = int(input())
answer = []

for i in range(t):
    n = int(input())
    arr = list(map(str, input().split()))
    Min = 9999999
    if n > 32:
        answer.append(0)
        continue

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                cnt = 0

                for x in range(4):
                    if arr[i][x] != arr[j][x]:
                        cnt += 1
                    if arr[i][x] != arr[k][x]:
                        cnt += 1
                    if arr[j][x] != arr[k][x]:
                        cnt += 1

                Min = min(Min, cnt)
    answer.append(Min)

for ans in answer:
    print(ans)
