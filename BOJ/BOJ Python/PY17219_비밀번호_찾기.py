n, m = map(int, input().split())
dict = {}
answer = []

for i in range(n):
    site, pw = input().split()
    dict[site] = pw

for i in range(m):
    site = input()
    answer.append(dict[site])

for ans in answer:
    print(ans)