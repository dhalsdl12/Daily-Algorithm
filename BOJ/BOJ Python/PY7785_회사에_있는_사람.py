n = int(input())
dic = {}

for i in range(n):
    name, el = input().split()

    if el == 'enter':
        dic[name] = 1
    elif el == 'leave':
        del dic[name]

dic = sorted(dic.keys(), reverse=True)
for d in dic:
    print(d)