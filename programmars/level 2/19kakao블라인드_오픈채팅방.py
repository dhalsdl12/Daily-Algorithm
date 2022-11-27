def solution(record):
    answer = []
    user = {}
    for s in record:
        re = list(s.split())
        if re[0] == 'Enter':
            user[re[1]] = re[2]
        elif re[0] == 'Change':
            user[re[1]] = re[2]
    for s in record:
        re = list(s.split())
        if re[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' %user[re[1]])
        elif re[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' %user[re[1]])
    return answer