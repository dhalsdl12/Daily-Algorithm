n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

m, k = map(int, input().split())
b = []
for i in range(m):
    b.append(list(map(int, input().split())))

c = [[0 for i in range(k)] for j in range(n)]

for N in range(n):
    for K in range(k):
        for M in range(m):
            c[N][K] += a[N][M] * b[M][K]

for N in range(n):
    for K in range(k):
        print(c[N][K], end=' ')
    print()