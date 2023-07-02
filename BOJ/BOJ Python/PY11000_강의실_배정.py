import heapq


n = int(input())
times = []
for i in range(n):
    s, t = map(int, input().split())
    times.append([s, t])
times.sort()

room = []
heapq.heapify(room)
heapq.heappush(room, times[0][1])
for i in range(1, n):
    if room[0] <= times[i][0]:
        heapq.heappop(room)
        heapq.heappush(room, times[i][1])
    else:
        heapq.heappush(room, times[i][1])
print(len(room))
