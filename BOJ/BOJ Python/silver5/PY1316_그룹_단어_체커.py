num = int(input())
cnt = 0
words = []

for i in range(num):
    words = input()
    for j in range(len(words)):
        if j != len(words)-1:
            if words[j] == words[j+1]:
                pass
            else:
                if words[j] in words[j+1:]:
                    break
        else:
            cnt += 1 
print(cnt)