from collections import deque
            

def solution(n, computers):
    def bfs(a):
        queue = deque()
        queue.append(a)
        visit[a] = 1
        while queue:
            tmp = queue.popleft()
            for i in range(n):
                if computers[i][tmp] == 1 and visit[i] == 0:
                    visit[i] = 1
                    queue.append(i)
                    
    answer = 0
    visit = [0 for _ in range(n)]
    
    for i in range(n):
        if visit[i] == 0:
            bfs(i)
            answer += 1
            
    return answer