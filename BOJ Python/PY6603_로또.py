from itertools import combinations

while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    del s[0]
    result = list(combinations(s, 6))

    for i in result:
        for j in i:
            print(j, end=' ')
        print()
    print()