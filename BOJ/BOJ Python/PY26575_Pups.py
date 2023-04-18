n = int(input())
answer = []

for _ in range(n):
    d, f, p = map(float, input().split())
    answer.append(d*f*p)

for ans in answer:
    print('$%.2f' % ans)