from collections import deque


def solution(rc, operations):
    answer = []
    row_l = len(rc)
    col_l = len(rc[0])
    
    center = deque(deque(row[1:-1]) for row in rc)
    first, last = deque(), deque()
    for i in range(row_l):
        first.append(rc[i][0])
        last.append(rc[i][col_l - 1])
    
    for oper in operations:
        if oper == 'ShiftRow':
            center.appendleft(center.pop())
            first.appendleft(first.pop())
            last.appendleft(last.pop())
        elif oper == 'Rotate':
            center[0].appendleft(first.popleft())
            last.appendleft(center[0].pop())
            center[row_l - 1].append(last.pop())
            first.append(center[row_l - 1].popleft())
    
    for i in range(row_l):
        cen = center[i]
        cen.appendleft(first[i])
        cen.append(last[i])
        answer.append(list(cen))
              
    return answer