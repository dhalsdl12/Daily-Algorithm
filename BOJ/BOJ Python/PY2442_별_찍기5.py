n = int(input())

for i in range(n):
    k = n - i - 1
    print(' ' * k + '*' * (2 * i + 1))