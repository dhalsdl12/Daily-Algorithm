result = []

while True:
    s = input()
    if s == '#':
        break
    cnt = 0
    for i in range(len(s)):
        if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or \
                s[i] == 'o' or s[i] == 'u':
            cnt += 1
        elif s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or \
                s[i] == 'O' or s[i] == 'U':
            cnt += 1
    result.append(cnt)
for re in result:
    print(re)
