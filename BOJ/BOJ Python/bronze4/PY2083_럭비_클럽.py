answer = []

while True:
    a, b, c = input().split()
    if a == '#' and b =='0' and c == '0':
        break
    age = int(b)
    weight = int(c)
    if age > 17 or weight >= 80:
        answer.append((a, 'Senior'))
    else:
        answer.append((a, 'Junior'))

for ans in answer:
    print(*ans)