def cnt(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return cnt(n-1) + cnt(n-2) + cnt(n-3)


num = int(input())
result = []
for i in range(num):
    number = int(input())
    result.append(cnt(number))

for i in result:
    print(i)
