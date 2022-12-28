num = int(input())
score = list(map(float, input().split()))
sum = 0
max = 0

for i in range(num):
    if score[i] > max:
        max = score[i]

for i in range(num):
    score[i] = (score[i]/max)*100
    sum += score[i]

avg = sum/num
print(avg)
