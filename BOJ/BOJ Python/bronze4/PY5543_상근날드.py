minb = 9999
mind = 9999
for i in range(3):
    n = int(input())
    minb = min(minb, n)

for i in range(2):
    n = int(input())
    mind = min(mind, n)

print(minb + mind - 50)