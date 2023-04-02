n = int(input())

station = {}

for i in range(n):
    station[input()] = []

r = int(input())
answer = []
for i in range(r):
    ans = 0
    check = list(input().split(' '))
    if check[0] == 'U':
        name = check[1]
        feature = list(check[2].split(','))
        station[name] = feature
    if check[0] == 'G':
        feature = list(check[1].split(','))
        
        for v in station.values():
            cnt = 0
            
            for f in feature:
                if f in v:
                    cnt += 1

            if cnt == len(feature):
                ans += 1
        answer.append(ans)

for aa in answer:
    print(aa)
