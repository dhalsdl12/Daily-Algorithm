from collections import deque
def bfs():
    while queue:
        a,b,c = queue.popleft()
        for i in range(6):
            x = a+dx[i]
            y = b+dy[i]
            z = c+dz[i]
            if 0<=x<n and 0<=y<m and 0<=z<h and s[z][x][y] == 0: #and visit[z][x][y] == 0:
                s[z][x][y] = s[c][a][b]+1
                #visit[z][x][y] = 1
                queue.append([x,y,z])
m,n,h = map(int, input().split())
dx,dy,dz = [1,-1,0,0,0,0],[0,0,1,-1,0,0],[0,0,0,0,1,-1]

s = [[] for p in range(h)]
#visit = [[[0 for i in range(m)]for j in range(n)]for _in range(h)]
queue = deque()

for i in range(h):
    for j in range(n):
        s[i].append(list(map(int, input().split())))

for z in range(h):
    for x in range(n):
        for y in range(m):
            if s[z][x][y] == 1:
                queue.append([x,y,z])
bfs()
TF = False
result = -2
for z in range(h):
    for x in range(n):
        for y in range(m):
            if s[z][x][y] == 0:
                TF = True
            result = max(result, s[z][x][y])

if TF == True:
    print(-1)
else:
    print(result-1)