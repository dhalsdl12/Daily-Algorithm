from collections import Counter


s = input()
cnt = Counter(s).items()
even, odd = 0, 0

for a in cnt:
    if a[1] % 2 == 0:
        even += 1
    elif a[1] % 2 != 0:
        odd += 1


if even > 0 and odd == 0:
    print('0')
elif odd > 0 and even == 0:
    print('1')
else:
    print('0/1')