num = int(input())

z = []
o = []
for i in range(num):
    n = int(input())
    zero = 1
    one = 0
    temp = 0
    for _ in range(n):
        temp = one
        one = one + zero
        zero = temp
    z.append(zero)
    o.append(one)

for i in range(num):
    print(z[i], o[i])