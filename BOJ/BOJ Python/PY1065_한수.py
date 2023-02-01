num = int(input())

cnt = 0

for i in range(1, num+1, 1):
    if i < 100:
        cnt += 1
    elif ((i%10) - ((i%100)//10)) == (((i%100)//10)-(i//100)):
        cnt += 1

print(cnt)