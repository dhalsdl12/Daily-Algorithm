from itertools import permutations


num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = int(input())
sign = input().split()
result = []
for per in permutations(num, n + 1):
    tmp = 0
    for i in range(n):
        if sign[i] == '<':
            if per[i] < per[i + 1]:
                continue
            else:
                tmp = 1
                break
        elif sign[i] == '>':
            if per[i] > per[i + 1]:
                continue
            else:
                tmp = 1
                break
    if tmp == 0:
        result.append(per)

print(''.join(map(str,list(max(result)))))
print(''.join(map(str,list(min(result)))))
        