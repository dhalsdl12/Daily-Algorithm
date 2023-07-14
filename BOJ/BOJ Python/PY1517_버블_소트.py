def merge_sort(start, end):
    global count, arr

    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid + 1, end)

        a, b = start, mid + 1
        temp = []

        while a <= mid and b <= end:
            if arr[a] <= arr[b]:
                temp.append(arr[a])
                a += 1
            else:
                temp.append(arr[b])
                b += 1
                count += (mid - a + 1)

        if a <= mid:
            temp = temp + arr[a:mid + 1]
        if b <= end:
            temp = temp + arr[b:end + 1]

        for i in range(len(temp)):
            arr[start + i] = temp[i]


count = 0
n = int(input())
arr = list(map(int, input().split()))
merge_sort(0, n - 1)
print(count)
