from collections import deque


def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append([begin, 0])
    visit = [0 for _ in range(len(words))]
    
    while queue:
        cur, cnt = queue.popleft()
        if cur == target:
            answer = cnt
            break
        for i in range(len(words)):
            check = 0
            if visit[i] == 0:
                for j in range(len(cur)):
                    if cur[j] != words[i][j]:
                        check += 1
                if check == 1:
                    queue.append([words[i], cnt + 1])
                    visit[i] = 1
    return answer