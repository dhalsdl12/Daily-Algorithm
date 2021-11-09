case = int(input())
result = []
for i in range(case):
    n, m = list(map(int, input().split()))
    li = list(map(int, input().split()))
    tmp = list(range(len(li)))
    tmp[m] = 'target'

    order = 0
    while True:
        if li[0] == max(li):
            order += 1

            if tmp[0] == 'target':
                result.append(order)
                break

            else:
                li.pop(0)
                tmp.pop(0)

        else:
            li.append(li.pop(0))
            tmp.append(tmp.pop(0))

for i in result:
    print(i)