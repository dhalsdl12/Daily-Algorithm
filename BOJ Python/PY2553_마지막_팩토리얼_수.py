num = int(input())

n = 1

for i in range(1, num+1):
    n *= i
    n %= 1000000000000

    while n%10 == 0:
        n /= 10
print(int(n%10))