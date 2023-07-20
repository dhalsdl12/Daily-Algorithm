p = int(input())
sw = 0
em = 0
ai = 0
no = 0

for _ in range(p):
    g, c, n = map(int, input().split())
    
    if g == 1:
        no += 1
    else:
        if c == 1 or c == 2:
            sw += 1
        elif c == 3:
            em += 1
        elif c == 4:
            ai += 1

print(sw)
print(em)
print(ai)
print(no)