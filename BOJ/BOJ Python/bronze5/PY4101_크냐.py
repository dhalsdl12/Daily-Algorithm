result = []
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a > b:
        result.append('Yes')
    else:
        result.append('No')

for re in result:
    print(re)
