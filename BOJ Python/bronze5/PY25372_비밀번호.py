n = int(input())
result = []
for i in range(n):
    s = input()
    if 6 <= len(s) <= 9:
        result.append('yes')
    else:
        result.append('no')

for re in result:
    print(re)