def solution(s):
    answer = []
    s = s.replace('{', '')
    s = s.split('}')
    for i in range(len(s)):
        if s[i] == '':
            s = s[:i]
            break
        else:
            s[i] = s[i].split(',')
            if i != 0:
                s[i].pop(0)
            s[i] = list(map(int, s[i]))
    
    s = sorted(s, key=len)
    dic = {}
    for i in s:
        for j in i:
            if j not in dic:
                answer.append(j)
                dic[j] = 1
    return answer