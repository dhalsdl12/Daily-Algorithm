import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

Min = min(map(min, arr))
Max = max(map(max, arr))
leastTime = 1e9
resultheight = 0

for i in range(Min, Max+1):
    plus = 0
    minus = 0
    for j in range(n):
        for k in range(m):
            height = arr[j][k]-i
            if height > 0:
                minus += height
            elif height < 0:
                plus += (-1*height)
    if minus+b >= plus:
        time = minus*2+plus

        if leastTime >= time:
            leastTime = time
            resultheight = i

print(leastTime, resultheight)
