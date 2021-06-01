from bisect import bisect_left

num = int(input())
a = list(map(int, input().split()))
stack = [-1000000001]

for i in a:
    if stack[-1] < i:
        stack.append(i)
    else:
        stack[bisect_left(stack, i)] = i

print(len(stack) - 1)