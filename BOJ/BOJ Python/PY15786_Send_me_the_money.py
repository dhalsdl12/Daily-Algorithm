n, m = map(int, input().split())
s = input()
answer = []

for i in range(m):
    ss = input()
    cnt = 0

    for cc in ss:
        if cc == s[cnt]:
            cnt += 1
        
        if cnt == n:
            break
    
    if cnt == n:
        answer.append('true')
    else:
        answer.append('false')

for ans in answer:
    print(ans)