def maxsize():
    max_s = 0
    stack = []

    for i in range(n):
        index = i
        while stack and stack[-1][0] >= rect[i]:
            h, index = stack.pop()
            size = h * (i-index)
            max_s = max(max_s, size)
        stack.append([rect[i], index])

    for h, left in stack:
        max_s = max(max_s, (n-left)*h)
    return max_s


result = []
while True:
    n, *rect = map(int, input().split())

    if n == 0:
        break
    result.append(maxsize())

for i in result:
    print(i)