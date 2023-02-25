import heapq


n = int(input())
arr = []
for i in range(n):
    heapq.heappush(arr, int(input()))


if len(arr) == 1:
    print(0)
else:
    answer = 0
    while True:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        answer += (a + b)
        heapq.heappush(arr, a + b)

        if len(arr) == 1:
            print(answer)
            break