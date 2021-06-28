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
xy = 1

result1 = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
result2 = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)

if result1 == 0 and result2 == 0:
    answer = True
    if min(x3, x4) <= max(x1, x2) and min(x1, x2) <= max(x3, x4)\
            and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
        xy = 0
        if max(x1, x2) == min(x3, x4) and max(y1, y2) == min(y3, y4) or\
            min(x1, x2) == max(x3, x4) and min(y1, y2) == max(y3, y4):
            xy = 1
        result = 1
if result1 <= 0 and result2 <= 0:
    if not answer:
        result = 1
print(result)
if result == 1 and xy == 1:
    if max(x1, x2) == min(x3, x4) and max(y1, y2) == min(y3, y4) or \
            min(x1, x2) == max(x3, x4) and min(y1, y2) == max(y3, y4):
        X, Y = max(x1, x2), max(y1, y2)
    else:
        A = y2 - y1
        B = x1 - x2
        E = A * x1 + B * y1
        C = y4 - y3
        D = x3 - x4
        F = C * x3 + D * y3
        DE = A * D - B * C
        X = ((E * D) - (B * F)) / DE
        Y = ((A * F) - (E * C)) / DE
    print(X, Y)

elif result == 1 and xy == 0:
    if y1 - y2 == 0:
        if y3 - y4 != 0:
            if x1 == x3 and y1 == y3:
                print(x1, y1)
            elif x1 == x4 and y1 == y4:
                print(x1, y1)
            elif x2 == x3 and y2 == y3:
                print(x2, y2)
            elif x2 == x4 and y2 == y4:
                print(x2, y2)
    elif y3 - y4 == 0:
        if y1 - y2 != 0:
            if x1 == x3 and y1 == y3:
                print(x1, y1)
            elif x1 == x4 and y1 == y4:
                print(x1, y1)
            elif x2 == x3 and y2 == y3:
                print(x2, y2)
            elif x2 == x4 and y2 == y4:
                print(x2, y2)
    elif (x1-x2)/(y1-y2) != (x3-x4)/(y3-y4):
        if x1 == x3 and y1 == y3:
            print(x1, y1)
        elif x1 == x4 and y1 == y4:
            print(x1, y1)
        elif x2 == x3 and y2 == y3:
            print(x2, y2)
        elif x2 == x4 and y2 == y4:
            print(x2, y2)
            