import sys

num = int(sys.stdin.readline())
time = []
cl = 1

for i in range(num):
    s, f = map(int, input().split())
    time.append((s, f))

time.sort(key = lambda x: x[0])
time.sort(key = lambda x: x[1])

finish = time[0][1]
for i in range(1, num):
    if time[i][0] < finish:
        continue
    else:
        finish = time[i][1]
        cl += 1
print(cl)