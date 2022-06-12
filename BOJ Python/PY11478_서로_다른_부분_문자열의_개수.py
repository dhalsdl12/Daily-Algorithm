s = input()
answer = set()
for i in range(len(s)):
    for j in range(i, len(s)):
        temp = s[i:j+1]
        answer.add(temp)
print(len(answer))
