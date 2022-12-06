n = int(input())
cnt = 1
prev = int(input())
for i in range(1, n):
    tmp = int(input())
    if tmp != prev:
        prev = tmp
        cnt += 1

print(cnt)