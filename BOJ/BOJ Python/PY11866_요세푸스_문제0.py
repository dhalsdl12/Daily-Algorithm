from collections import deque
n,k = map(int, input().split())
deque = deque()
count = []
for i in range(n):
    deque.append(i+1)
print('<', end = '')

while deque:
    for i in range(k-1):
        deque.append(deque[0])
        deque.popleft()
    count.append(deque.popleft())
for i in range(len(count)-1):
    print(count[i], end = ', ')
print(count[len(count)-1], end = '>')