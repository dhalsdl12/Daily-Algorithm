answer = []

while True:
    s = input()
    if s == '***':
        break
    answer.append(s[::-1])

for ans in answer:
    print(ans)