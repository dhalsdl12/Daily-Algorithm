def solve(depth, n, m):
    if depth == m:
        print(' '.join(map(str, out)))
        return
    for i in range(n):
        if len(out) == 0 or out[-1] <= i+1:
            out.append(i + 1)
            solve(depth + 1, n, m)
            out.pop()


n, m = map(int, input().split())

out = []

solve(0, n, m)