from collections import deque


def bfs(a):
    queue = deque()
    queue.append((a, ''))
    visit = set()
    visit.add(a)
    MAX = 10e9

    while queue:
        s, op = queue.popleft()

        if s == t:
            return op
        
        ns = s * s
        if 0 <= ns <= MAX and ns not in visit:
            queue.append((ns, op + '*'))
            visit.add(ns)

        ns = s + s
        if 0 <= ns <= MAX and ns not in visit:
            queue.append((ns, op + '+'))
            visit.add(ns)

        ns = 1
        if ns not in visit:
            queue.append((ns, op + '/'))
            visit.add(ns)
    
    return -1


s, t = map(int, input().split())
if s == t:
    print(0)
else:
    print(bfs(s))