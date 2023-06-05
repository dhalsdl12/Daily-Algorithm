n = int(input())
s, t = '', ''
i = 0
j = n - 1

for _ in range(n):
    s += input()

while i <= j:
    if s[i] < s[j]:
        t += s[i]
        i += 1
    elif s[i] > s[j]:
        t += s[j]
        j -= 1
    else:
        ti, tj = i, j
        tmp = 0

        while ti <= tj:
            if s[ti] < s[tj]:
                tmp = 1
                t += s[i]
                i += 1
                break
            elif s[ti] > s[tj]:
                tmp = 1
                t += s[j]
                j -= 1
                break
            else:
                ti += 1
                tj -= 1
        
        if tmp == 0:
            t += s[i]
            i += 1

for i in range(n):
    print(t[i], end='')
    if (i + 1) % 80 == 0:
        print()