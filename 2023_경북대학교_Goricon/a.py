arr = list(map(int, input().split()))

sum_arr = sum(arr[:-1])
check = arr[-1] * 4

if check > sum_arr:
    print(check - sum_arr)
else:
    print(0)