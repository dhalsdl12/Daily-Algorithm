n = int(input())
m = int(input())
s = input()

IOI = 'IO' * n + 'I'
cnt = 0

for i in range(0, m - n - 1, 1):
    tmp = s[i : i + len(IOI)]
    if IOI == tmp:
        cnt += 1

print(cnt)