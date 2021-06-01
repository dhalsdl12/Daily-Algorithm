from collections import deque

def bfs(node, dp):
    q = deque()
    q.append((node, dp))
    while q:
        node, dp = q.popleft()
        for n in [node+1, node*2, node*3]:
            if n <= num and check[n] == 0:
                if n == num:
                    return check[node] + 1, dp+[n]
                q.append((n, dp+[n]))
                check[n] = check[node] + 1


num = int(input())
if num == 1:
    print(0)
    print(1)
else:
    check = [0]*(num+1)
    cnt, dp = bfs(1, [1])
    print(cnt)
    for i in range(len(dp)-1, -1, -1):
        print(dp[i], end=' ')