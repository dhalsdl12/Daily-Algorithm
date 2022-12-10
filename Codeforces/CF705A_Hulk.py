n = int(input())

str1 = 'I hate '
str2 = 'that I love '
str3 = 'that I hate '
str4 = 'it'

if n == 1:
    print(str1 + str4)
elif n % 2 == 0:
    a = n // 2
    for i in range(a - 1):
        str1 += (str2 + str3)
    str1 += (str2 + str4)
    print(str1)
else:
    a = n // 2
    for i in range(a):
        str1 += (str2 + str3)
    print(str1 + str4)