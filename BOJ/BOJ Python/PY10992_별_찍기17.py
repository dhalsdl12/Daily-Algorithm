n = int(input())

for i in range(1, n + 1):
    if i == n:
        print('*' * (i * 2 - 1))
    elif i  == 1:
        print(' ' * (n - 1) + '*')
    else:
        print(' ' * (n - i) + '*' + ' ' * (i * 2 - 3) + '*')