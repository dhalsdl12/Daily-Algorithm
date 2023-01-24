from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def next_square(step):
            quot, rem = divmod(step-1, rows)
            row = (rows - 1) - quot
            if row%2 != rows%2:
                col = rem 
            else:
                col = (rows - 1) - rem
            return row, col


        rows = len(board)
        total_square = rows*rows

        dist = {1: 0}
        queue = collections.deque([1])
        while queue:
            square = queue.popleft()

            if square == total_square:
                return dist[square]

            for new_square in range(square+1, min(square+6, total_square) + 1):
                r, c = next_square(new_square)
                
                if board[r][c] != -1:
                    new_square = board[r][c]
                if new_square not in dist:
                    dist[new_square] = dist[square] + 1
                    queue.append(new_square)
        return -1
