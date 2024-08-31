n, r, s = input().split()
a, b = 0, 0
dic_a = {}
dic_b = {}

for i in range(int(n)):
    if r[i] == s[i]:
        a += 1
    else:
        if r[i] not in dic_a:
            dic_a[r[i]] = 1
        if s[i] not in dic_b:
            dic_b[s[i]] = 1

for items in dic_b:
    if items in dic_a:
        b += 1

print(a, b)