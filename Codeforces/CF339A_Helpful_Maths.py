s = input()

if len(s) == 1:
    print(s)

else:
    a = []
    for c in s:
        if c == '+':
            continue
        a.append(c)
    a.sort()
    string = ''
    for aa in a:
        string += (aa + '+')
    print(string[:-1])