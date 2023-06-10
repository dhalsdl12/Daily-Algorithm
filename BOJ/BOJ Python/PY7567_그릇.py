s = input()
answer = 0
tmp = ''

for i in range(len(s)):
    if i == 0:
        tmp = s[i]
        answer += 10
        continue
    
    if s[i] == tmp:
        answer += 5
    else:
        tmp = s[i]
        answer += 10

print(answer)
