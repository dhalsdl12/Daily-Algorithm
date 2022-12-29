num = 9
score = []
cnt = 0

for i in range(num):
    score.append(int(input()))
max = score[0]

for i in range(num):
    if score[i] > max:
        max = score[i]
        cnt = i

print(max)
print(cnt+1)