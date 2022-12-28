yn = []
while(True):
    sentence = input()
    if sentence == '.':
        break
    stack = []
    temp = 1
    for i in sentence:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0 or stack[-1] == '[':
                temp = 0
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if len(stack) == 0 or stack[-1] == '(':
                temp = 0
                break
            elif stack[-1] == '[':
                stack.pop()
    if temp == 1 and len(stack) == 0:
        yn.append('yes')
    else:
        yn.append('no')
for i in range(len(yn)):
    print(yn[i])