def solve(depth, n, m):
    if depth == m:
        print(' '.join(map(str, out)))
        return
    for i in arr:
        if len(out) == 0 or out[-1] <= i:
         out.append(i)
         solve(depth + 1, n, m)
         out.pop()


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
out = []
solve(0, n, m)