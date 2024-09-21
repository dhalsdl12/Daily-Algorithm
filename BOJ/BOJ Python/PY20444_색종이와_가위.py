n, k = map(int, input().split())
left = 0
right = n // 2

check = False

while left <= right:
    mid = (left + right) // 2
    piece = (mid + 1) * (n - mid + 1)

    if piece == k:
        print('YES')
        check = True
        break

    if k > piece:
        left = mid + 1
    else:
        right = mid - 1


if not check:
    print('NO')