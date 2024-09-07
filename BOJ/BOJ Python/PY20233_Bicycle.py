a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())

if t - 30 <= 0:
    sum_a = a
else:
    sum_a = a + (t - 30) * 21 * x

if t - 45 <= 0:
    sum_b = b
else:
    sum_b = b + (t - 45) * 21 * y
print(sum_a, sum_b)