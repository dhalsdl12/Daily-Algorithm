n, m = map(int, input().split())
name = []
name2 = []
for i in range(n):
    name.append(input().strip())
for i in range(m):
    name2.append(input().strip())
result = list(set(name) & set(name2))
print(len(result))
for i in sorted(result):
    print(i)
