a, b = map(int,input().split())
pokemon1 = {}
pokemon2 = {}
result = []
for i in range(a):
    name = input().rstrip()
    pokemon1[i+1] = name
    pokemon2[name] = i+1

for i in range(b):
    tmp = input().rstrip()
    if tmp.isdigit():
        result.append(pokemon1[int(tmp)])
    else:
        result.append(pokemon2[tmp])

for i in result:
    print(i)
