from collections import deque


def bfs():
    queue = deque()
    queue.append((n, 0))
    visit = set()
    answer = []

    while queue:
        number, cnt = queue.popleft()

        if cnt == k:
            answer.append(number)
            continue
        
        string = list(str(number))
        
        for i in range(l):
            for j in range(i + 1, l):
                if i == 0 and string[j] == '0':
                    continue

                string[i], string[j] = string[j], string[i]
                num = int(''.join(string))

                if (num, cnt + 1) not in visit:
                    visit.add((num, cnt + 1))
                    queue.append((num, cnt + 1))

                string[i], string[j] = string[j], string[i]

    return answer


n, k = map(int, input().split())
l = len(str(n))

answer = bfs()

if len(answer) == 0:
    print(-1)
else:
    print(max(answer))