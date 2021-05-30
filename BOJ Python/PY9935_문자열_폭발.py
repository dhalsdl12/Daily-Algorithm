st = input().strip()
re = input().strip()

stack = []
for i in range(len(st)):
    stack.append(st[i])

    if(len(stack) >= len(re)):
        tmp = "".join(stack[-len(re):])
        if(tmp == re):
            cnt = 0
            while cnt < len(re):
                stack.pop()
                cnt += 1
if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack)) 
