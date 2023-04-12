t = int(input())
answer = []

for _ in range(t):
    m, n, x, y = map(int, input().split())
    ans = -1
    
    while x <= m * n:
        if (x - y) % n == 0:
            ans = x
            break
        
        x += m

    answer.append(ans)

for ans in answer:
    print(ans)