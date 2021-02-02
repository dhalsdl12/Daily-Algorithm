import sys

n = int(sys.stdin.readline())
num1 = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
num2 = map(int, sys.stdin.readline().split())

n_cnt = {}
for n in num1:
    try:
        n_cnt[n] += 1
    except:
        n_cnt[n] = 1

ans = []
for m in num2:
    try:
        ans.append(n_cnt[m])
    except:
        ans.append(0)

for i in ans:
    print(i, end = ' ')