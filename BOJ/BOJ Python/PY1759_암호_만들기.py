from itertools import combinations
l,c = map(int,input().split())

char = list(input().split())
char.sort()
result = []
aeiou = {'a','e','i','o','u'}
pw = list(combinations(char, l))

for c in pw:
    diff = set(c).difference(aeiou)
    if 2<=len(diff)<=l-1:
        result.append(c)
for i in result:
    print(i)