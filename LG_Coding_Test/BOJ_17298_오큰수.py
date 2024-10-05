n = int(input())
arr = list(map(int, input().split()))
answer = [-1 for _ in range(n)]
stack = []

for i in range(n):
    while len(stack) != 0 and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    
    stack.append(i)

for ans in answer:
    print(ans, end=' ')
