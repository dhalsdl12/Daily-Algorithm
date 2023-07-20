def solution(dartResult):
    num = 0
    result = []
    for d in dartResult:
        check = 0
        if d.isdigit():
            num *= 10
            num += int(d)
        else:
            if d == 'S':
                result.append(num)
            elif d == 'D':
                result.append(num ** 2)
            elif d == 'T':
                result.append(num ** 3)
            elif d == '*':
                result[len(result) - 1] *= 2
                if len(result) != 1:
                    result[len(result) - 2] *= 2
            elif d == '#':
                result[len(result) - 1] *= -1
            num = 0
    return sum(result)