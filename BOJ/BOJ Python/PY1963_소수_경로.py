from collections import deque

# 에라토스테네스의 체
def findPrime():
    for i in range(2, 100):
        if prime[i] == 0:
            for j in range(2 * i, 10000, i):
                prime[j] = 1


def bfs():
    queue = deque()
    queue.append((a, 0))

    visit = [0 for _ in range(10000)]
    visit[a] = 1

    while queue:
        num, cnt = queue.popleft()
        strnum = str(num)

        if num == b:
            return cnt
        
        for i in range(4):
            for j in range(10):
                tmp = int(strnum[:i] + str(j) + strnum[i + 1:])

                if visit[tmp] == 0 and prime[tmp] == 0 and tmp >= 1000:
                    visit[tmp] = 1
                    queue.append((tmp, cnt + 1))


t = int(input())
answer = []
prime = [0 for _ in range(10000)]

findPrime()
for _ in range(t):
    a, b = map(int, input().split())
    ans = bfs()
    if ans == None:
        answer.append('Impossible')
    else:
        answer.append(ans)

for ans in answer:
    print(ans)