num = int(input())

n = 1

for i in range(1, num+1):
    n *= i
    while n % 10 == 0:
        n /= 10
    n %= 1000000000000
n %= 100000
print("%05d" % int(n))