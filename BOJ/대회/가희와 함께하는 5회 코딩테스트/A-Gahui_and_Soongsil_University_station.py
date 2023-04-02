answer = 0

for i in range(4):
    a, b = input().split()

    if a == 'Es':
        answer += (int(b) * 21)        
    elif a == 'Stair':
        answer += (int(b) * 17)

print(answer)