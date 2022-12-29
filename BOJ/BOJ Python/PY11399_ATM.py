num = int(input())
s = 0
time = list(map(int, input().split()))
time.sort()

for i in range(num):
    for j in range(i+1):
        s += time[j]
print(s)