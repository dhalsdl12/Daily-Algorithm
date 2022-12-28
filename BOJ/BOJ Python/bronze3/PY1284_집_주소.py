result = []
while True:
    s = 0
    cnt = 0
    number = int(input())
    if number == 0:
        break
    while True:
        a = number % 10
        cnt += 1
        if a == 1:
            s += 2
        elif a == 0:
            s += 4
        else:
            s += 3
        number //= 10
        if number == 0:
            break
    result.append(s + cnt + 1)
for re in result:
    print(re)