import math

num = int(input())
n = []
m = []
result = []

for i in range(num):
    a, b = map(int, input().split())
    n.append(a)
    m.append(b)

for i in range(num):
    result.append(math.factorial(m[i])/((math.factorial(n[i]))*(math.factorial(m[i]-n[i]))))

for i in range(num):
    print(int(result[i]))  