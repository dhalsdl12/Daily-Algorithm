string = input()
a = 'YONSEI'
b = 'KOREA'
ac = 0
bc = 0

for s in string:
    if s == a[ac]:
        ac += 1
    elif s == b[bc]:
        bc += 1
    
    if ac == 6:
        print('YONSEI')
        break
    elif bc == 5:
        print('KOREA')
        break