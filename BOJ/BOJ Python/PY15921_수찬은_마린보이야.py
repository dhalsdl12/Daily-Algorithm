n = int(input())

if n == 0:
    print('divide by zero')
else:
    arr = list(map(int, input().split()))
    avg = sum(arr) / n / (sum(arr) / n)
    print('%.2f' %avg)