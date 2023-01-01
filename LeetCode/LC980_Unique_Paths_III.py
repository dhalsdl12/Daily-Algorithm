class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(r, c, cnt):
            cnt -= 1
            if r == fr and c == fc:
                if cnt == 0:
                    self.answer += 1
                return
            grid[r][c] = -1
            for i in range(4):
                dr = r + dx[i]
                dc = c + dy[i]
                if 0 <= dr < len(grid) and 0 <= dc < len(grid[0]) and grid[dr][dc] != -1:
                    dfs(dr, dc, cnt)
            grid[r][c] = 0


        cnt = 0
        self.answer = 0
        sr, sc, fr, fc = -1, -1, -1, -1
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != -1:
                    cnt += 1
                if grid[i][j] == 1:
                    sr, sc = i, j
                elif grid[i][j] == 2:
                    fr, fc = i, j
        
        dfs(sr, sc, cnt)

        return self.answer
