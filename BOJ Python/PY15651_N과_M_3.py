def solve(depth, n, m):
    if depth == m:
        print(' '.join(map(str, out)))
        return
    for i in range(n):
        out.append(i+1)
        solve(depth+1, n, m)
        out.pop()


n, m = map(int, input().split())

out = []

solve(0, n, m)