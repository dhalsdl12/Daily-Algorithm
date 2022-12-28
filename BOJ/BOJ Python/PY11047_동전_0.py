import sys

num, money = map(int, sys.stdin.readline().split())
coin = []
cnt = 0

for i in range(num):
    coin.append(int(input()))

coin.sort(reverse=True)

for i in range(num):
    s = 0
    if money/coin[i] > 0:
        s = money//coin[i]
        money = money - coin[i]*s
        cnt += s
    else:
        continue

print(cnt)