def solution(lottos, win):
    answer = []
    cnt = 0
    cnt_z = lottos.count(0)
    
    for l in lottos:
        if l in win:
            cnt += 1
            
    answer.append(7 - (cnt + cnt_z))
    answer.append(7 - cnt)
    if(answer[1] > 6):
        answer[1] = 6
    if(answer[0] > 6):
        answer[0] = 6
    
    return answer
