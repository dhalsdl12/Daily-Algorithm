num = int(input())

result = []

for i in range(num):
    cnt = 0
    score = list(map(int, input().split()))
    zz = score.pop(0)
    avg = sum(score)/zz

    for j in range(zz):
        if score[j] > avg:
            cnt += 1
    cnt = (cnt/zz)*100
    result.append(cnt)

for i in range(num):
    print('%0.3f' % result[i]+"%")
