n = int(input())
answer = 99999

for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        continue
    answer = min(answer, b)

if answer == 99999:
    print(-1)
else:
    print(answer)