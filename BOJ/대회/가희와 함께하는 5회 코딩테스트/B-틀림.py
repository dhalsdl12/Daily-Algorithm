import heapq


c, h = map(int, input().split())
heap = []

answer = 24 * 60 * 60

for _ in range(c):
    hh, m, s = map(int, input().split(':'))
    heapq.heappush(heap, hh * 24 * 60 * 60 + m * 60 + s)

for _ in range(h):
    hh, m, s = map(int, input().split(':'))
    heapq.heappush(heap, hh * 24 * 60 * 60 + m * 60 + s)

while True:
    if len(heap) == 1:
        answer -= 40
        break
    if heap[1] - heap[0] < 40:
        answer -= (heap[1] - heap[0])
        heapq.heappop(heap)
    elif heap[1] - heap[0] >= 40:
        heapq.heappop(heap)
        answer -= 40
print(answer)