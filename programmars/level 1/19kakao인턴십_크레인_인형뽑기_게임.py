def solution(board, moves):
    answer = 0
    bucket = []
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] > 0:
                bucket.append(board[i][m-1])
                board[i][m-1] = 0
                if bucket[-1:] == bucket[-2:-1]:
                    answer += 1
                    bucket = bucket[:-2]
                break
    return answer*2
