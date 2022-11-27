import heapq
import sys

num = int(sys.stdin.readline())
arr = []
result = []

i = 0
while i < num:
    n = int(sys.stdin.readline())

    if n == 0:
        if arr:
            result.append(heapq.heappop(arr))
        else:
            result.append(0)
    else:
        heapq.heappush(arr, n)
    i += 1
for i in range(len(result)):
    print(result[i])