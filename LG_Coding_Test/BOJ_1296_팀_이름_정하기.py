yeondu = input()
n = int(input())
arr = []
answer = ''
max_ans = -1

for i in range(n):
    arr.append(input())
arr = sorted(arr)

for i in range(n):
    s = arr[i]
    love = {'L':0, 'O':0, 'V':0, 'E':0}

    for yeon in yeondu:
        if yeon in love:
            love[yeon] += 1
    
    for c in s:
        if c in love:
            love[c] += 1
    
    avg = ((love['L'] + love['O']) * (love['L'] + love['V']) * (love['L'] + love['E']) * (love['O'] + love['V']) * (love['O'] + love['E']) * (love['V'] + love['E'])) % 100

    if avg > max_ans:
        max_ans = avg
        answer = s
        
print(answer)