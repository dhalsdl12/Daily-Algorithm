n = int(input())
result = 'NO'
for i in range(2, n, 2):
    if (n - i) % 2 == 0:
        result = 'YES'
        break

print(result)