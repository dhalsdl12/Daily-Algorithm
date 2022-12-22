n = int(input())

for i in range(n):
    k = n - i - 1
    print(' ' * i + '*' * (k * 2 + 1))