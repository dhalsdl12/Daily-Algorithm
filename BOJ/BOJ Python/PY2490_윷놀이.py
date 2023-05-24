answer = []
check = {0 : 'E', 1 : 'A', 2 : 'B', 3 : 'C', 4 : 'D'}

for _ in range(3):
    arr = list(map(int, input().split()))
    a = arr.count(0)

    answer.append(check[a])

for ans in answer:
    print(ans)