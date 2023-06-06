n = int(input())
answer = []

for _ in range(n):
    s = input()
    c = len(s) // 2

    if s[c - 1] == s[c]:
        answer.append('Do-it')
    else:
        answer.append('Do-it-Not')

for ans in answer:
    print(ans)