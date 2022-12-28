n = int(input())

gra = []
result = []

gra.append(0)
for i in range(n):
    gra.append(int(input()))

result.append(0)
result.append(gra[1])
if n > 1:
    result.append(gra[1] + gra[2])

for i in range(3, n+1):
    result.append(max(result[i-1], result[i-3]+gra[i-1]+gra[i],
                      result[i-2]+gra[i]))

print(result[n])
