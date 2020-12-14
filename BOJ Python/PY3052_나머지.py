num = 10
score = []

for i in range(num):
    num1 = int(input())
    num1 = num1%42
    score.append(num1)

score = set(score)              #set은 배열내 중복을 제거해준다.
print(len(score))