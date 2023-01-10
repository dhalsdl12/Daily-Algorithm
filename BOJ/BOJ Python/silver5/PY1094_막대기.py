n = int(input())
cnt = 0
while True:
    if n % 2 == 1:
        cnt += 1
    n //= 2
    if n == 0:
        break
print(cnt)
