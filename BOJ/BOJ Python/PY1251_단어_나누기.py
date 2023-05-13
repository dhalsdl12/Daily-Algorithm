string = list(input())
answer = []
tmp = []

for i in range(1, len(string)):
    for j in range(i + 1, len(string)):
        a = string[:i]
        b = string[i:j]
        c = string[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        tmp.append(a + b + c)

for t in tmp:
    answer.append(''.join(t))

print(sorted(answer)[0])