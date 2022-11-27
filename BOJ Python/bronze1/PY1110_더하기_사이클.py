num = temp = int(input())

cnt = 0
new2 = 0

if num < 10:
    num = num*10

while True:
    ten = num//10
    one = num%10

    new = ten + one

    cnt += 1

    num = int(str(num%10) + str(new%10))

    if temp == num:
        break

print(cnt)