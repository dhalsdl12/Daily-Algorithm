import sys


def isPrime(n):
    sieve = [1] * (n + 1)

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * 2, n + 1, i):
                sieve[j] = 0

    return [i for i in range(2, n + 1) if sieve[i]]


num = int(sys.stdin.readline())
cnt = 0
prime = isPrime(num)

for i in range(len(prime)):
    sum = 0
    for j in range(i, len(prime)):
        sum += prime[j]
        if sum > num:
            break
        elif sum == num:
            cnt += 1
            break
print(cnt)