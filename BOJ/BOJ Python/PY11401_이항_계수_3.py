#페르마의 소정리
#(a/b)%p
# = (a * b^-1) % p
# = (a * b^-1 * b^(p-1)) % p
# = (a * b^(p-2)) % p
# = (a % p) * (b^(p-2) % p) % p

def pow(a,b):
    if b == 0:
        return 1
    if b % 2 == 1:
        return (pow(a, b//2)**2*a)%p
    else:
        return (pow(a, b//2)**2)%p


n, k = map(int, input().split())
p = 1000000007
factorial = [1 for i in range(n+1)]

for i in range(2, n+1):
    factorial[i] = factorial[i-1]*i % p

A = factorial[n]
B = (factorial[n-k]*factorial[k])%p

print((A%p) * (pow(B, p-2) % p) %p)