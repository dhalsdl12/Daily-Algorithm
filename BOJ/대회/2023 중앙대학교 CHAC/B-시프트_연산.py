from collections import deque


def bfs():
    queue = deque()
    queue.append((arr, ''))

    while queue:
        tmp, s = queue.popleft()
        if sum(tmp) == 0:
            return s
        check = -1
        for i in range(n):
            if tmp[i] == 1:
                check = i
                break
        if check < n // 2:
            tmp2 = tmp[1:]
            tmp2.append(0)
            queue.append((tmp2, s + 'L'))
        if check >= n // 2:
            tmp3 = [0] + tmp[:-1]
            queue.append((tmp3, s + 'R'))

n = int(input())
arr = list(map(int, input().split()))
string = bfs()
print(len(string))
print(string)