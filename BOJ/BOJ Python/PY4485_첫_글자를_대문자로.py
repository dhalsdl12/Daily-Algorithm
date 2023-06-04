n = int(input())
answer = []

for _ in range(n):
    s = input()
    tmp = s[0].upper()
    answer.append(tmp + s[1:])

for ans in answer:
    print(ans)