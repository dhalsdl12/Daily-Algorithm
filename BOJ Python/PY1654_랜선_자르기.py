n, k = map(int, input().split())

li = []
for i in range(n):
    li.append(int(input()))

start = 1
end = max(li)

while start <= end:
    mid = (start + end) // 2
    lines = 0

    for i in li:
        lines += (i // mid)

    if lines >= k:
        start = mid + 1
    else:
        end = mid - 1

print(end)