s = input()
a = 0
b = 0
for c in s:
    if c == 'A':
        a += 1
    else:
        b += 1

print(str(a) + ' : ' + str(b))