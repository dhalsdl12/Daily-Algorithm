num = int(input())
result = []
cnt = 0
cnt2 = 0

for i in range(num):
    score = 0
    string = input()
    for a in string:
        if a == 'O':
            cnt += 1
            cnt2 += cnt
        else:
            cnt = 0
    result.append(cnt2)
    cnt = 0
    cnt2 = 0

for i in range(len(result)):
    print(result[i])