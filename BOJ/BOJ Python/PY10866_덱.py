import sys
from collections import deque
def push(deque, x, command):
    if command == "push_front":
        return deque.appendleft(x)
    else:
        return deque.append(x)
def pop(deque, command):
    if len(deque) == 0:
        return -1
    else:
        if command == "pop_front":
            return deque.popleft()
        else:
            return deque.pop()

def size(deque):
    return len(deque)
def empty(deque):
    if len(deque) == 0:
        return 1
    else:
        return 0
def fb(deque, command):
    if len(deque) == 0:
        return -1
    else:
        if command == "back":
            return deque[len(deque)-1]
        else:
            return deque[0]

num = int(sys.stdin.readline().rstrip())
deque = deque()
result = []
for i in range(num):
    order = sys.stdin.readline().rstrip().split()
    command = order[0]
    if command == "push_front" or command == "push_back":
        push(deque, order[1], command)
    elif command == "pop_front" or command == "pop_back":
        result.append(pop(deque, command))
    elif command == "empty":
        result.append(empty(deque))
    elif command == "size":
        result.append(size(deque))
    elif command == "front" or command == "back":
        result.append(fb(deque, command))
for i in range(len(result)):
    print(result[i])