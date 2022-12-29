n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sortA = sorted(a, reverse=True)
sortB = sorted(b)
sum = 0
for i in range(n):
    sum += sortA[i]*sortB[i]
print(sum)