from collections import Counter


def solution(N, stages):
    answer = []
    result = []
    number = len(stages)
    ans = Counter(stages)
    for i in range(N):
        if number == 0:
            result.append([i+1, 0.0])
        else:
            result.append([i+1, ans[i+1]/number])
        number -= ans[i+1]
    result.sort(key=lambda x:x[1], reverse=True)
    for i in range(len(result)):
        answer.append(result[i][0])
    return answer