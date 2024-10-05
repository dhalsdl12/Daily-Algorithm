def dfs(x, y, cnt):
    global answer
    answer = max(answer, cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c:
            if visited[ord(arr[nx][ny]) - 65] == 0:
                visited[ord(arr[nx][ny]) - 65] = 1
                dfs(nx, ny, cnt + 1)
                visited[ord(arr[nx][ny]) - 65] = 0
       
r, c = map(int, input().split())
arr = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(r):
    arr.append(list(input().rstrip()))

visited = [0 for _ in range(26)]
visited[ord(arr[0][0]) - 65] = 1
answer = 0

dfs(0, 0, 1)
print(answer)