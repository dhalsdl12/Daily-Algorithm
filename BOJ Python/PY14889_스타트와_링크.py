import sys
from itertools import combinations

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

candidate = [i for i in range(n)]
result = sys.maxsize

for comb in combinations(candidate, n//2):
    start = set(comb)
    link = set(candidate) - start
    start = list(start)
    link = list(link)

    sl = 0
    for i in range(1, n//2):
        for j in range(i):
            sl += (arr[start[i]][start[j]] + arr[start[j]][start[i]])
            sl -= (arr[link[i]][link[j]] + arr[link[j]][link[i]])
    result = min(result, abs(sl))

print(result)
