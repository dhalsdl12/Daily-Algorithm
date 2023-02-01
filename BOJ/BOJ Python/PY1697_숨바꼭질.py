from collections import deque

n,k = map(int, input().split())
queue = deque()
visit = [0 for i in range(100001)]

queue.append([n,0])
while queue:
    spot, cnt = queue[0][0], queue[0][1]
    if spot == k:
        break
    queue.popleft()
    visit[spot] = 1

    if spot-1 >=0 and visit[spot-1] == 0:
        queue.append([spot-1, cnt+1])
    if spot+1 <= 100000 and visit[spot+1] == 0:
        queue.append([spot+1, cnt+1])
    if spot*2 <= 100000 and visit[spot*2] == 0:
        queue.append([2*spot, cnt+1])
print(queue[0][1])