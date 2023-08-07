n = int(input())
arr = []
check = -1

for i in range(n):
    s = input()
    arr.append(s)

    if s == '?':
        check = i
if n == 1:
    m = int(input())
    print(input())
    exit()
if check == 0:
    last = arr[check + 1][0]
    m = int(input())

    for i in range(m):
        A = input()
        
        if A in arr:
            continue

        if A[-1] == last:
            print(A)
            exit()
elif check == n - 1:
    first = arr[check - 1][-1]
    m = int(input())

    for i in range(m):
        A = input()
        
        if A in arr:
            continue

        if A[0] == first:
            print(A)
            exit()
else:
    first = arr[check - 1][-1]
    last = arr[check + 1][0]
    m = int(input())

    for i in range(m):
        A = input()
        
        if A in arr:
            continue

        if A[0] == first and A[-1] == last:
            print(A)
            exit()