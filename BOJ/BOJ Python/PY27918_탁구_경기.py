n = int(input())
arr = [input() for _ in range(n)]
d, p = 0, 0

for i in arr:
    if i == "D":
        d += 1
    else:
        p += 1

    if abs(d - p) == 2:
        break

print(str(d) + ':' + str(p))