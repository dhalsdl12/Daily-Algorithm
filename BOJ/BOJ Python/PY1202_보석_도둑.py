import heapq


n, k = map(int, input().split())
dia = []
for _ in range(n):
    w, v = map(int, input().split())
    heapq.heappush(dia, [w, v])

bag = []
for _ in range(k):
    c = int(input())
    heapq.heappush(bag, c)

total_value = 0
c_dia = []

for i in range(k):
    c = heapq.heappop(bag)
    while dia and c >= dia[0][0]:
        [w, v] = heapq.heappop(dia)
        heapq.heappush(c_dia, -v)
    if c_dia:
        total_value -= heapq.heappop(c_dia)
    elif not dia:
        break

print(total_value)
