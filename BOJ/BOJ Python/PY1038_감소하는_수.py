from itertools import combinations

n = int(input())
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
number = []

for i in range(1, 11, 1):
    comb = combinations(num, i)
    for c in comb:
        c = list(c)
        c.sort(reverse=True)
        number.append(int(''.join(map(str, c))))

number.sort()
if n < len(number):
    print(number[n])
else:
    print(-1)
