n = int(input())
answer = []

for i in range(n):
    s = 'Case #' + str(i + 1) + ': '

    tmp = list(input().split())
    tmp = tmp[::-1]
    s += (' '.join(tmp))

    answer.append(s)

for ans in answer:
    print(ans)