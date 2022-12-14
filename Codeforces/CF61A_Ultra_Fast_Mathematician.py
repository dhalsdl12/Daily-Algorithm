a = input()
b = input()
result = ''
for i in range(len(a)):
    if int(a[i]) + int(b[i]) == 1:
        result += '1'
    else:
        result += '0'
print(result)