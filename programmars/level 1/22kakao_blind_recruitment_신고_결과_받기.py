def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dic = {id: [] for id in id_list}
    result = {}
    for i in range(len(id_list)):
        result[id_list[i]] = 0
    for re in set(report):
        a, b = re.split()
        dic[a].append(b)
    for key, val in dic.items():
        for v in val:
            result[v] += 1
    for key, val in dic.items():
        for v in val:
            if result[v] >= k:
                answer[id_list.index(key)] += 1

    return answer