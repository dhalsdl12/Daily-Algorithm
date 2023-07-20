from collections import deque


def solution(n, m, x, y, r, c, k):
    # n, m 세로 가로
    # x, y 출발지
    # r, c 도착지
    # k 거리
    def Distance(x, y, r, c):
        return abs(r - x) + abs(c - y)

    def bfs():
        queue = deque([])
        queue.append([x, y, 0, ''])
        
        while queue:
            a, b, cnt, s = queue.pop()
            if a == r and b == c:
                if cnt == k:
                    return s
                elif (k - cnt) % 2 == 1:
                    return 'impossible'
            tmp = []
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0 < nx <= n and 0 < ny <= m and Distance(nx, ny, r, c) + cnt < k:
                    tmp.append([nx, ny, cnt + 1, s + dirs[i]])
            tmp.reverse()
            queue += tmp
        return 'impossible'
    
    dirs = ['d', 'l', 'r', 'u']
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    
    return bfs()