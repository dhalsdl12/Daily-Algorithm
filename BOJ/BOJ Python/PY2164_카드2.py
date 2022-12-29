import sys
from collections import deque

num = int(sys.stdin.readline())
deque = deque()
cnt = 1
for i in range(num):   
    deque.append(i+1)
while True:
    if len(deque) == 1:
        print(deque[0])
        break
    elif cnt%2 != 0:
        deque.popleft()
        cnt+=1
    elif cnt%2 == 0:
        number = deque.popleft()
        deque.append(number)
        cnt+=1