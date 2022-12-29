from _collections import defaultdict


n = int(input())
a = int(input())
lista = list(map(int, input().split()))
b = int(input())
listb = list(map(int, input().split()))

dicta = defaultdict(int)
result = 0
for i in range(a):
    for j in range(i, a):
        dicta [sum(lista[i:j+1])] += 1
for i in range(b):
    for j in range(i, b):
        result += dicta[n - sum(listb[i:j+1])]

print(result)
