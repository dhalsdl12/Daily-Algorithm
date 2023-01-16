def fib(n):
    global cnt1
    if n == 1 or n == 2:
        cnt1 += 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


n = int(input())
fibo = [0, 1]

cnt1 = 0
cnt2 = 0

fib(n)
for i in range(2, n):
    fibo.append(fibo[i - 1] + fibo[i - 2])
    cnt2 += 1

print(cnt1, cnt2)
