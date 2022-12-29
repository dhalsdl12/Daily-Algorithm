def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x : (x[col - 1], -x[0]))
    for i in range(row_begin, row_end + 1):
        result = 0
        for a in data[i - 1]:
            result += (a % i)
        answer ^= result
    return answer