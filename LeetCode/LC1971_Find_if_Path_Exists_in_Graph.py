class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        q = deque([source])
        visit = [0 for i in range(n)]
        nei = defaultdict(list)

        for n1, n2 in edges:
            nei[n1].append(n2)
            nei[n2].append(n1)

        while q:
            node = q.popleft()
            if node == destination:
                return True
            
            for n in nei[node]:
                if visit[n] == 0:
                    visit[n] = 1
                    q.append(n)
        
        return False