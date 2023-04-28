y, m, d = map(int, input().split())

yy, mm, dd = map(int, input().split())

if m < mm:
    print(yy - y)
elif m == mm:
    if d <= dd:
        print(yy - y)
    else:
        print(yy - y - 1)
else:
    print(yy - y - 1)
print(yy - y + 1)
print(yy - y)