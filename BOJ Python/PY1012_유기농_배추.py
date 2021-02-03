def bfs(a,b):
    queue = [[a,b]]
    s[a][b] = 0

    while queue:
        x,y = queue[0][0], queue[0][1]
        del queue[0]
        for d in range(4):
            x1 = x+dx[d]
            y1 = y+dy[d]
            if 0<=x1<m and 0<=y1<n and s[x1][y1] == 1:
                s[x1][y1] = 0
                queue.append([x1,y1])
    cnt.append(1)

t = int(input())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
result = []
for i in range(t):
    cnt = []
    m,n,k = map(int, input().split())
    s = [[0] * n for _ in range(m)]

    for j in range(k):
        x, y = map(int, input().split())
        s[x][y] = 1
    
    for a in range(m):
        for b in range(n):
            if s[a][b] == 1:
                bfs(a,b)
    result.append(len(cnt))
for i in result:
    print(i)