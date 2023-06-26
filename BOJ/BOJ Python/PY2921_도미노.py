n = int(input())

answer = 0

for i in range(1, n + 1):
    answer += 1.5 * i * (i + 1)

print(int(answer))