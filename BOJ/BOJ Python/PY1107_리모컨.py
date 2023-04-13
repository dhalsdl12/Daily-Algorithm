n = int(input())
m = int(input())

if m != 0:
    arr = list(map(int, input().split()))
else:
    arr = []

min_cnt = abs(100 - n)

for i in range(1000001):
    number = str(i)

    for j in range(len(number)):
        if int(number[j]) in arr:
            break
        elif j == len(number) - 1:
            min_cnt = min(min_cnt, abs(int(number) - n) + len(number))

print(min_cnt)