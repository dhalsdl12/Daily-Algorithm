num = int(input())
number = 0
for i in range(1, num+1):
    div_num = list(map(int, str(i)))
    sum_num = i + sum(div_num)
    if sum_num == num:
        number = i
        break

print(number)