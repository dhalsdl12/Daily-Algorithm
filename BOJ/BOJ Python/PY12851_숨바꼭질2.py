from collections import deque


def bfs():
    answer = 999999
    count = 0
    queue = deque([(n, 0)])
    visit[n] = 0
    while queue:
        x, cnt = queue.popleft()
        if answer < cnt:
            continue
        if x == k:
            if answer > cnt:
                answer = cnt

            if answer == cnt:
                count += 1

        for nx in [x - 1, x + 1, x * 2]:
            if 0 <= nx <= 100000 and (visit[nx] == -1 or visit[nx] == cnt + 1):
                queue.append((nx, cnt + 1))
                visit[nx] = cnt + 1

    return answer, count


n, k = map(int, input().split())
visit = [-1 for _ in range(100001)]
answer, count = bfs()

print(answer)
print(count)