t = int(input())

for _ in range(t):
    answer = []
    
    n = int(input())
    i = 0
    while True:
        tmp = n % 2
        if tmp == 1:
            answer.append(i)
        
        i += 1
        n //= 2

        if n == 0:
            break

    print(*answer)