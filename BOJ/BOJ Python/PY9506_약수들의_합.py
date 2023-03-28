answer = []
while True:
    n = int(input())
    arr = []
    if n == -1:
        break

    for i in range(1, n):
        if n % i == 0:
            arr.append(i)
    
    if sum(arr) == n:
        string = str(n) + ' = '

        for i in range(len(arr)):
            if i == len(arr) - 1:
                string += (str(arr[i]))
            else:
                string += (str(arr[i]) + ' + ')
    else:
        string = str(n) + ' is NOT perfect.'

    answer.append(string)

for ans in answer:
    print(ans)