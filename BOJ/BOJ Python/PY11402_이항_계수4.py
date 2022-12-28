def calculation(n, k):
    if n < k:
        return 0
    elif n == k:
        return 1
    else:
        ans = 1
        for i in range(1, k+1):
            ans *= (n - i + 1)
            ans //= i
        return ans


n, k, m = map(int, input().split())
list_n = []
list_k = []

while n != 0 or k != 0:
    list_n.append(n % m)
    list_k.append(k % m)
    n //= m
    k //= m

result = 1
for i in range(len(list_n)):
    ni = list_n[i]
    ki = list_k[i]
    result *= calculation(ni, ki)
    result %= m

print(result)
