import math
num = int(input())
fac = math.factorial(num)
cnt = 0

if num == 0:
    print(0)
else:
    fac = list(str(fac))

    for i in range(len(fac)):
        if fac[len(fac)-1-i] == '0':
            cnt += 1
        else:
            break
    print(cnt)