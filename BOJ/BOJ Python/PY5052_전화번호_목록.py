t = int(input())
answer = []

for _ in range(t):
    n = int(input())
    phone = []
    check = 0

    for i in range(n):
        phone.append(input())
    
    phone.sort()
    
    for i in range(n - 1):
        if phone[i] == phone[i + 1][0 : len(phone[i])]:
            answer.append('NO')
            check = 1
            break
    if check == 0:
        answer.append('YES')

for ans in answer:
    print(ans)