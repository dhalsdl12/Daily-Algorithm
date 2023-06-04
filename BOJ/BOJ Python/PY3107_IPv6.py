ip = list(input().split(':'))

answer = ['' for _ in range(8)]
output = ''
index = 0
check = 0

for i in range(len(ip)):
    tmp = ip[i]

    if len(tmp) == 4:
        answer[index] = tmp
        index += 1
    elif len(tmp) > 0:
        answer[index] = '0' * (4 - len(tmp)) + tmp
        index += 1
    else:
        if check == 0:
            for j in range(8 - len(ip) + 1):
                answer[index] = '0000'
                index += 1
            check = 1
        else:
            answer[index] = '0000'
            index += 1

for ans in answer:
    output += (ans + ':')

print(output[:-1])