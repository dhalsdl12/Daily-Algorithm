p = int(input())
c = int(input())

answer = 0

if p > c:
    answer += 500

print(answer + p * 50 - c * 10)