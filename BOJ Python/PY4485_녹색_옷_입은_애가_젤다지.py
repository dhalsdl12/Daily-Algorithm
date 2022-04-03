from heapq import heappush, heappop

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    dp = [[100000000] * n for i in range(n)]
    dp[0][0] = Map[0][0]

    heap = []
    heappush(heap, [Map[0][0], 0, 0])

    visit = [[0] * n for i in range(n)]
    visit[0][0] = 1

    while heap:
        r, x, y = heappop(heap)

        for cnt in range(4):
            x1 = x + dx[cnt]
            y1 = y + dy[cnt]

            if 0 <= x1 < n and 0 <= y1 < n:
                if visit[x1][y1] == 0:
                    dp[x1][y1] = min(dp[x][y] + Map[x1][y1], dp[x1][y1])
                    heappush(heap, [dp[x1][y1], x1, y1])
                    visit[x1][y1] = 1
    return dp[n-1][n-1]


result = []
cnt = 0
while True:
    n = int(input())
    if n == 0:
        break
    Map = []
    for i in range(n):
        Map.append(list(map(int, input().split())))
    result.append(bfs())
    cnt += 1

for i in range(cnt):
    print("Problem %d: %d" %(i+1, result[i]))
