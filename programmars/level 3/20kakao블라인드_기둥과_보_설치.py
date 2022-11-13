def check(answer):
    for x, y, a in answer:
        if a == 0:
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            else:
                return False
        elif a == 1:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 1:
            answer.append([x, y, a])
            if not check(answer):
                answer.pop()
        elif b == 0:
            answer.remove([x, y, a])
            if not check(answer):
                answer.append([x, y, a])
    answer.sort()
    return answer