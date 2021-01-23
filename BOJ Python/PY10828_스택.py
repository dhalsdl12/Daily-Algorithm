import sys
def push(num):
    stack.append(num)
def pop():
    if len(stack) == 0:
        return -1
    else:
        return stack.pop()
def size():
    return len(stack)
def empty():
    if len(stack) == 0:
        return 1
    else:
        return 0
def top():
    if len(stack) == 0:
        return -1
    else:
        return stack[len(stack)-1]

num = int(sys.stdin.readline().rstrip())
stack = []
stack_num = []
for i in range(num):
    input_split = sys.stdin.readline().rstrip().split()

    order = input_split[0]
    if order == "push":
        push(input_split[1])
    elif order == "pop":
        stack_num.append(pop())
    elif order == "size":
       stack_num.append(size())
    elif order == "empty":
        stack_num.append(empty())
    elif order == "top":
        stack_num.append(top())

for i in range(len(stack_num)):
    print(stack_num[i])