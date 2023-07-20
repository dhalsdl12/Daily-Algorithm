from collections import deque

def solution(queue1, queue2):
    answer = 0
    a = deque(queue1)
    b = deque(queue2)
    sum_a = sum(a)
    sum_b = sum(b)
    for i in range(len(queue1) * 3):
        if sum_a == sum_b:
            return i
        elif sum_a > sum_b:
            num = a.popleft()
            b.append(num)
            sum_a -= num
            sum_b += num
        else:
            num = b.popleft()
            a.append(num)
            sum_a += num
            sum_b -= num
        
    return -1