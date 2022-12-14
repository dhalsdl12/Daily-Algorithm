n = int(input())

arr = [100, 20, 10, 5, 1]
sum = 0
for a in arr:
    sum += n // a
    n %= a
print(sum)