import sys

n = int(sys.stdin.readline())
queue = []
result = []
for i in range(n):
    string = sys.stdin.readline().split()

    if string[0] == "push":
        queue.insert(0, string[1])
    elif string[0] == "pop":
        if len(queue) != 0:
            result.append(queue.pop())
        else:
            result.append(-1)
    elif string[0] == "size":
        result.append(len(queue))
    elif string[0] == "empty":
        if len(queue) == 0:
            result.append(1)
        else:
            result.append(0)
    elif string[0] == "front":
        if len(queue) != 0:
            result.append(queue[-1])
        else:
            result.append(-1)
    elif string[0] == "back":
        if len(queue) != 0:
            result.append(queue[0])
        else:
            result.append(-1)

for i in result:
    print(i)