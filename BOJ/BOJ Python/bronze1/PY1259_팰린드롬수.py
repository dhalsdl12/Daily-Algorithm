result = []
cnt = 0
while True:
    cnt = 0
    word = input()
    if word == "0":
        break
    for i in range(len(word)//2):
        if word[i] != word[(-i-1)]:
            result.append("no")
            cnt = 1
            break
    if cnt == 1:
        continue
    result.append("yes")

for i in result:
    print(i)