a, b = map(int, input().split())
answer = ''
while True:
    aa, bb = a % 10, b % 10

    c = str(aa + bb)
    answer = c + answer

    a //= 10
    b //= 10

    if a == 0 or b == 0:
        break

if a != 0:
    answer = str(a) + answer
elif b != 0:
    answer = str(b) + answer

print(answer)