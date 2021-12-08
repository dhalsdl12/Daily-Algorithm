m = int(input())
S = set()
result = []
for _ in range(m):
    tmp = input().strip().split()
    if len(tmp) == 1:
        if tmp[0] == "all":
            for i in range(1, 21):
                S = set([i])
        else:
            S = set()

    else:
        func, x = tmp[0], tmp[1]
        x = int(x)

        if func == "add":
            S.add(x)
        elif func == "remove":
            S.discard(x)
        elif func == "check":
            if x in S:
                result.append("1")
            else:
                result.append("0")
        elif func == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)
for i in result:
    print(i)
