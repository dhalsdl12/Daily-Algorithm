from itertools import combinations

n, m = map(int, input().split())

C = combinations(range(1, n+1), m)

for i in C:
    print(' '.join(map(str, i)))
