num = int(input())
number = []
sum = 0
for i in range(num):
    a = int(input())
    if a != 0:
        number.append(a)
    else:
        number.pop()
for i in range(len(number)):
    sum += number[i]
print(sum)