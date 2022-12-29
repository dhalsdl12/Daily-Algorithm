from collections import deque
import sys
def bfs():
    queue = deque()
    queue.append([0,0,1])
    visit = [[[0]*2 for i in range(m)]for i in range(n)]
    visit[0][0][1] = 1
    while queue:
        a,b,w = queue.popleft()
        if a == n-1 and b == m-1:
            return visit[a][b][w]
        for i in range(4):
            x = a+dx[i]
            y = b+dy[i]
            if 0<=x<n and 0<=y<m:
                if s[x][y] == "1" and w== 1:
                    visit[x][y][0] = visit[a][b][1]+1
                    queue.append([x,y,0])
                elif s[x][y] == "0" and visit[x][y][w] == 0:
                    visit[x][y][w] = visit[a][b][w]+1
                    queue.append([x,y,w])
    return -1

n,m = map(int, sys.stdin.readline().split())
s = []
dx, dy = [1,-1,0,0],[0,0,1,-1]
for i in range(n):
    s.append(list(sys.stdin.readline()))

print(bfs())