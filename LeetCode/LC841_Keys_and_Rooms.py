class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(node):
            if visit[node] == 1:
                return 
            visit[node] = 1
            for room in rooms[node]:
                if visit[room] == 1:
                    continue
                dfs(room)

        visit = [0 for _ in range(len(rooms))]
        dfs(0)

        if 0 in visit:
            return False
        return True