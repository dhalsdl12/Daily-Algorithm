num = int(input())

n = 2

while num != 1:
    if num%n == 0:
        print(n)
        num /= n
        continue
    else:
        n += 1