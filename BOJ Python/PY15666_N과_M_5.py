def solve(depth, n, m):
    if depth == m:
        print(' '.join(map(str, out)))
        return
    overlap = 0
    for i in range(n):
        if (len(out) == 0 or out[-1] <= arr[i]) \
                and overlap != arr[i]:
            out.append(arr[i])
            overlap = arr[i]
            solve(depth + 1, n, m)
            out.pop()


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
out = []
solve(0, n, m)