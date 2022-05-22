import sys


def dist(d1, d2):
    return (d1[0] - d2[0]) ** 2 + (d1[1] - d2[1]) ** 2


def solve(dot, n):
    if n == 2:
        return dist(dot[0], dot[1])
    elif n == 3:
        return min(dist(dot[0], dot[1]), dist(dot[1], dot[2]),
                   dist(dot[0], dot[2]))

    mid = (dot[n//2][0] + dot[n//2-1][0])//2
    d = min(solve(dot[:n//2], n//2), solve(dot[n//2:], n//2))

    check = []
    for sub in dot:
        if (mid-sub[0])**2 <= d:
            check.append(sub)
    check.sort(key=lambda x: x[1])

    if len(check) == 1:
        return d
    else:
        y_check = d
        for i in range(len(check)-1):
            for j in range(i+1, len(check)):
                if (check[i][1] - check[j][1])**2 > d:
                    break
                elif check[i][0] < mid and check[j][0] < mid:
                    continue
                elif check[i][0] > mid and check[j][0] > mid:
                    continue
                y_check = min(y_check, dist(check[i], check[j]))
    return y_check


n = int(sys.stdin.readline())
dot = []
for i in range(n):
    dot.append(list(map(int, sys.stdin.readline().split())))

dot_set = list(set(map(tuple, dot)))
if len(dot_set) != len(dot):
    result = 0
else:
    dot_set.sort()
    result = solve(dot_set, n)

print(result)
