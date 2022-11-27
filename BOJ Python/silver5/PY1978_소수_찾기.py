num = int(input())
cnt = 0
numbers = list(map(int, input().split()))

for num1 in numbers:
    for i in range(2, num1 +1):
        if num1 % i == 0:
            if i != num1:
                break
            else:
                cnt += 1

print(cnt)