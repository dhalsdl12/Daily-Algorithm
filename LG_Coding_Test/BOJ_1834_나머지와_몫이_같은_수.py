n = int(input())
answer = 0

for i in range(1, n):
    answer += (i * n + i)

print(answer)