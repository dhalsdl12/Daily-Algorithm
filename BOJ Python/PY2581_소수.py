num1 = int(input())
num2 = int(input())

sum1=0
min1=num2

for i in range(num1, num2+1):
    for j in range(2, i+1):
        if i % j == 0:
            if j != i:
                break
            else:
                sum1 += i
                if i < min1:
                    min1 = i

if sum1 != 0:
    print(sum1)
    print(min1)
else:
    print("-1")