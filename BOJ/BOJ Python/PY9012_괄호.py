num =  int(input())
YN = []
for i in range(num):
    vps = input()
    sum = 0
    for s in vps:
        if s == '(':
            sum += 1
        elif s == ')':
            sum -= 1
        if sum < 0:
            YN.append('NO')
            break
    if sum > 0:
        YN.append('NO')
    elif sum == 0:
        YN.append('YES')
for i in range(num):
    print(YN[i])