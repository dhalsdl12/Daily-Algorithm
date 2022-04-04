import sys


def dist(d1, d2):
    return (d1[0] - d2[0]) ** 2 + (d1[1] - d2[1]) ** 2


def divide(start, end):
    if start == end:
        return float('inf')

    if end - start == 1:
        return dist(dot[start], dot[end])

    mid = (start + end)//2
    minDist = min(divide(start, mid), divide(mid, end))

    target_dot = []
    for i in range(start, end+1):
        if (dot[mid][0] - dot[i][0]) ** 2 < minDist:
            target_dot.append(dot[i])

    target_dot.sort(key=lambda x: x[1])

    t = len(target_dot)
    for i in range(t-1):
        for j in range(i+1, t):
            if (target_dot[i][1] - target_dot[j][1]) ** 2 < minDist:
                minDist = min(minDist, dist(target_dot[i], target_dot[j]))
            else:
                break
    return minDist


n = int(sys.stdin.readline())
dot = []
for i in range(n):
    dot.append(list(map(int, sys.stdin.readline().split())))
dot.sort()
result = divide(0, n-1)
print(result)
