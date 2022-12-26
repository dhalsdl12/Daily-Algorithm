n = int(input())

for i in range(n):
    k = n - i - 1
    print(' ' * k + '*' * ((i + 1) * 2 - 1))
for i in range(n - 2, -1, -1):
    k = n - i - 1
    print(' ' * k + '*' * ((i + 1) * 2 - 1))
