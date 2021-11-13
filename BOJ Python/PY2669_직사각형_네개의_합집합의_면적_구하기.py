xy = [[0 for _ in range(100)] for _ in range(100)]
count = 0

for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            if xy[x][y] == 0:
                count += 1
                xy[x][y] = 1

print(count)
