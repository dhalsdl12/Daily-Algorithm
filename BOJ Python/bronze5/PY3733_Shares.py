result = []

while True:
    try:
        n, x = map(int, input().split())
        result.append(x // (n + 1))
    except:
        for x in result:
            print(x)
        break

