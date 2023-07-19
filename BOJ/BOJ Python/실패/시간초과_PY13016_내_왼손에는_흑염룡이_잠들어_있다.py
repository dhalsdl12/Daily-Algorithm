def dfs(node):
    global visit
    for nxt, cost in arr[node]:
        if visit[nxt] > visit[node] + cost:
            visit[nxt] = visit[node] + cost
            dfs(nxt)


n = int(input())
arr = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b, l = map(int, input().split())
    arr[a].append((b, l))
    arr[b].append((a, l))

answer = []
for i in range(1, n + 1):
    visit = [9999999 for _ in range(n + 1)]
    visit[i] = 0
    dfs(i)
    answer.append(max(visit[1:]))


for ans in answer:
    print(ans)