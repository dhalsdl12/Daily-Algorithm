n = int(input())
arr = list(map(int, input().split()))
answer = 0
tmp = []

for a in arr:
    if a % 2 == 0:
        answer += a
    else:
        tmp.append(a)

if len(tmp) % 2 == 0:
    print(answer + sum(tmp))
else:
    tmp.sort(reverse=True)
    tmp.pop()

    print(answer + sum(tmp))
