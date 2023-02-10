n = int(input())
arr = []
ab = set()
Max = 0
for _ in range(n):
    arr.append(int(input()))

for i in range(n):
    for j in range(n):
        ab.add(arr[i] + arr[j])
for i in range(n - 1, -1, -1):
    for j in range(n):
        if (arr[i] - arr[j]) in ab:
            Max = max(Max, arr[i])

print(Max)