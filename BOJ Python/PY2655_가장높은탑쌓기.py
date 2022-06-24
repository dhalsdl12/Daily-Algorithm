n = int(input())
arr = [(0, 0, 0, 0)]

for i in range(n):
    s, h, w = map(int, input().split())
    arr.append((i + 1, s, h, w))
arr.sort(key=lambda x: x[3])
'''
for a in arr:
    print(a)
'''
dp = [0 for i in range(n + 1)]

for i in range(1, n+1):
    for j in range(0, i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j] + arr[i][2])

result = []
max_h = max(dp)
idx = dp.index(max_h)
'''
print(max_h)
print(idx)
print(dp)
'''
while True:
    if max_h == dp[idx]:
        result.append(arr[idx][0])
        max_h -= arr[idx][2]
    idx -= 1
    if idx == 0:
        break

print(len(result))
for i in range(len(result)-1, -1, -1):
    print(result[i])

