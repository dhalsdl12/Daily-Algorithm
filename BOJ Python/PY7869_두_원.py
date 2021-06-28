import math

x1, y1, r1, x2, y2, r2 = map(float, input().split())

d = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))

if d > r1+r2:
    print("0.000")

elif d <= abs(r1-r2):
    if r1 >= r2:
        s = math.pi*r2*r2
        s = float(round(1000 * s) / 1000)
        print("%.3f" % s)
    else:
        s = math.pi*r1*r1
        s = float(round(1000 * s) / 1000)
        print("%.3f" % s)
else:
    a1 = (math.acos((r1 * r1 + (d * d) - r2 * r2) / (2 * r1 * d))) * 2
    a2 = (math.acos((r2 * r2 + (d * d) - r1 * r1) / (2 * r2 * d))) * 2

    area1 = 0.5 * a1 * r1 * r1 - 0.5 * r1 * r1 * math.sin(a1)
    area2 = 0.5 * a2 * r2 * r2 - 0.5 * r2 * r2 * math.sin(a2)

    s = area1 + area2
    s = float(round(1000*s)/1000)
    print("%.3f" % s)
