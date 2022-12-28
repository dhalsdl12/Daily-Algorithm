a = input()

stack = []
print_stack = ''
for x in a:
    if x == '+' or x == '-' or x == '*' or x == '/' or x == '(' or x == ')':
        if x == '(':
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                print_stack += stack.pop()
            stack.pop()
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                print_stack += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                print_stack += stack.pop()
            stack.append(x)
    else:
        print_stack += x
while stack:
    print_stack += stack.pop()
print(print_stack)