import heapq


n = int(input())
heap = []

for _ in range(n):
    number = map(int, input().split())
    for num in number:
        if len(heap) < n:
            heapq.heappush(heap, num)
        else:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

print(heap[0])