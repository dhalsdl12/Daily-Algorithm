import sys

num = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
result = [-1 for _ in range(num)]
stack = []

for i in range(num):
    while len(stack) != 0 and num_list[stack[-1]] < num_list[i]:
        result[stack.pop()] = num_list[i]

    stack.append(i)

for i in range(num):
    print(result[i], end = ' ')