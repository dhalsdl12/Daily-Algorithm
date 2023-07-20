def solution(today, terms, privacies):
    def days(date):
        y, m, d = map(int, date.split('.'))
        return y * 12 * 28 + m * 28 + d
    
    answer = []
    todays = days(today)
    
    term_dic = {}
    for term in terms:
        t, m = term.split()
        term_dic[t] = int(m) * 28
        
    for i, privacy in enumerate(privacies):
        d, t = privacy.split()
        day = days(d) + term_dic[t]
        
        if todays >= day:
            answer.append(i + 1)
        
        
    return answer