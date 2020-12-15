num = int(input())

count = 1
upcount = 6
cnt = 1

while count < num:
    count += upcount
    upcount += 6
    cnt += 1

print(cnt)