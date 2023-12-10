n = int(input())

answer = []

for i in range(n):
    a, b, x = map(int, input().split())

    answer.append(a * (x - 1) + b)

for ans in answer:
    print(ans)