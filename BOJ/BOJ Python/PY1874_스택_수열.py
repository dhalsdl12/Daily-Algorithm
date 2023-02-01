num = int(input())

count = 0
stack = []
result = []
no_message = True

for i in range(num):
    x = int(input())

    while count < x:
        count += 1
        stack.append(count)
        result.append('+')
    