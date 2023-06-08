n = int(input())
s = input()

for i in range(n):
    tmp = s[i:]
    ns = tmp.count('s')
    nt = tmp.count('t')
    
    if ns == nt:
        print(tmp)
        break