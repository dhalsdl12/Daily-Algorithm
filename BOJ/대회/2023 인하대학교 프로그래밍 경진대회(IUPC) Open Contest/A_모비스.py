string = input()
mobis = "MOBIS"
check = 0

for m in mobis:
    if m not in string:
        check = 1
        break

if check == 0:
    print('YES')
else:
    print('NO')