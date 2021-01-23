from collections import Counter
num = int(input())
count = []
for i in range(num):
    n = int(input())
    clothes = []

    for j in range(n):
        name, cloth = input().split()
        clothes.append(cloth)
    cnt = 1
    result = Counter(clothes)
    for key in result:
        cnt *= result[key]+1
    count.append(cnt)

for i in range(num):
    print(count[i]-1)