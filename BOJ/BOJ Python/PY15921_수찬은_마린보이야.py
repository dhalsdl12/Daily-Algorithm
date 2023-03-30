n = int(input())

if n == 0:
    print('divide by Zeor')
else:
    arr = list(map(int, input().split()))
    avg = sum(arr) / n / (sum(arr) / n)
    print('%.2f' %avg)