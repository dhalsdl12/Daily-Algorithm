s = input().upper()
dic = {}
answer = ''
max_ans = 0
check = 0

for c in s:
    if c not in dic:
        dic[c] = 1
    else:
        dic[c] += 1

for item, key in dic.items():
    if key > max_ans:
        max_ans = key
        answer = item
        check = 1
    elif key == max_ans:
        check = 2

if check == 1:
    print(answer)
else:
    print('?')