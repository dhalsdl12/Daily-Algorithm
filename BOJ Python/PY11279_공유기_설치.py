import heapq
import sys
num = int(sys.stdin.readline())
arr = []
i = 0

while i < num:
    n = int(sys.stdin.readline())
    if n:
        heapq.heappush(arr, [-n,n])
    else:
        if arr:
            print(heapq.heappop(arr)[1])
        else:
            print('0')
    i += 1