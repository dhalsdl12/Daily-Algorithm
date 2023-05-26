import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}

for _ in range(n):
    v = input().strip()
    if len(v) >= m:
        if v not in dic:
            dic[v] = 1
        else:
            dic[v] += 1

s_dic = sorted(dic.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for a in s_dic:
    print(a[0])