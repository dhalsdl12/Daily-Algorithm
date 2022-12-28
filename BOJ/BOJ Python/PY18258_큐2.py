import sys
from collections import deque
def push(deque, x):
    return deque.append(x)
def pop(deque):
    if len(deque) == 0:
        return -1
    else:
        return deque.popleft()
def size(deque):
    return len(deque)
def empty(deque):
    if len(deque) == 0:
        return 1
    else:
        return 0
def front(deque):
    if len(deque) == 0:
        return -1
    else:
        return deque[0]
def back(deque):
    if len(deque) == 0:
        return -1
    else:
        return deque[len(deque)-1]


num = int(sys.stdin.readline().rstrip())
deque = deque()
print_num=[]
for i in range(num):
    order = sys.stdin.readline().rstrip().split()
    command = order[0]
    if(command == "push"):
        push(deque, order[1])
    elif(command == "pop"):
        print_num.append(pop(deque))
    elif(command == "size"):
        print_num.append(size(deque))
    elif(command == "empty"):
        print_num.append(empty(deque))
    elif(command == "front"):
        print_num.append(front(deque))
    elif(command == "back"):
        print_num.append(back(deque))

for i in range(len(print_num)):
    print(print_num[i])