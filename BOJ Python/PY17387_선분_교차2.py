def ccw(x1, y1, x2, y2, a, b):
    ans = (x2 - x1) * (b - y1) - (y2 - y1) * (a - x1)
    if ans < 0:
        return -1
    elif ans > 0:
        return 1
    else:
        return 0


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
answer = False
result = 0

result1 = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
result2 = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)

if result1 == 0 and result2 == 0:
    answer = True
    if min(x3, x4) <= max(x1, x2) and min(x1, x2) <= max(x3, x4)\
            and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
        result = 1
if result1 <= 0 and result2 <= 0:
    if not answer:
        result = 1
print(result)