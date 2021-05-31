def solve(depth, n, m):
    if depth == m:
        print(' '.join(map(str, out)))
        return
    for i in range(n):
        if visit[i] == False:
            out.append(arr[i])
            visit[i] = True
            solve(depth + 1, n, m)
            out.pop()
            visit[i] = False


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visit = [False] * n
out = []
solve(0, n, m)