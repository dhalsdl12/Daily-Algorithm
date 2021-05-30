from itertools import permutations

n, m = map(int, input().split())

P = permutations(range(1, n+1), m)
for i in P:
    print(' '.join(map(str, i)))