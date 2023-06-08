n = int(input())
s = input()

answer = 0

for i in range(n // 2):
    if s[i] != s[-1 - i]:
        answer += 1

print(answer)