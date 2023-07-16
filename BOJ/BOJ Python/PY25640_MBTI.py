mbti = input()
n = int(input())
answer = 0

for i in range(n):
    s = input()

    if mbti == s:
        answer += 1

print(answer)