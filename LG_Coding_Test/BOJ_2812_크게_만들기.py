n, k = map(int, input().split())
num = input().rstrip()
stack = []
answer = ''

for i in range(n):
    while k > 0 and len(stack) != 0 and int(stack[-1]) < int(num[i]):
        stack.pop()
        k -= 1
    
    stack.append(num[i])

for i in range(len(stack) - k):
    answer += stack[i]

print(answer)