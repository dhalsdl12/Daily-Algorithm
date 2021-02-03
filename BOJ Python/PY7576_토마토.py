from collections import deque
def bfs():
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            x,y = a+dx[i], b+dy[i]
            if 0<=x<n and 0<=y<m and s[x][y] == 0:
                s[x][y] = s[a][b]+1
                queue.append([x,y])


m,n = map(int, input().split())
dx,dy = [1,-1,0,0],[0,0,1,-1]
s = []
queue = deque()

for i in range(n):
    s.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if s[i][j] == 1:
            queue.append([i,j])
bfs()
TF = False
result = -2
for i in range(n):
    for j in range(m):
        if s[i][j] == 0:
            TF = True
        result = max(result, s[i][j])

if TF == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result-1)