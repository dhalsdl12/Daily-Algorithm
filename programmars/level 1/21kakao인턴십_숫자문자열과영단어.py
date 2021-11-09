def solution(s):
    answer = 0
    check = ''
    
    for i in s:
        if i.isdigit():
            if check == "zero":
                answer *= 10
                answer += 0
                answer *= 10
                answer += int(i)
                check = ''
            elif check == "one":
                answer *= 10
                answer += 1
                answer *= 10
                answer += int(i)
                check = ''
            elif check == "two":
                answer *= 10
                answer += 2
                answer *= 10
                answer += int(i)
                check = ''
            elif check == "three":
                answer *= 10
                answer += 3
                answer *= 10
                answer += int(i)
                check = ''
            elif check == "four":
                answer *= 10
                answer += 4
                answer *= 10
                answer += int(i)
                check = ''
            elif check == "five":
                answer *= 10
                answer += 5
                answer *= 10
                answer += int(i)
                check = ''
            elif check == "six":
                answer *= 10
                answer += 6
                answer *= 10
                answer += int(i)
                check = ''
            elif check == "seven":
                answer *= 10
                answer += 7
                answer *= 10
                answer += int(i)
                check = ''
            elif check == "eight":
                answer *= 10
                answer += 8
                answer *= 10
                answer += int(i)
                check = ''
            elif check == "nine":
                answer *= 10
                answer += 9
                answer *= 10
                answer += int(i)
                check = ''
            else:
                answer *= 10
                answer += int(i)
                check = ''
        elif check == "zero":
            answer *= 10
            answer += 0
            check = i
        elif check == "one":
            answer *= 10
            answer += 1
            check = i
        elif check == "two":
            answer *= 10
            answer += 2
            check = i
        elif check == "three":
            answer *= 10
            answer += 3
            check = i
        elif check == "four":
            answer *= 10
            answer += 4
            check = i
        elif check == "five":
            answer *= 10
            answer += 5
            check = i
        elif check == "six":
            answer *= 10
            answer += 6
            check = i
        elif check == "seven":
            answer *= 10
            answer += 7
            check = i
        elif check == "eight":
            answer *= 10
            answer += 8
            check = i
        elif check == "nine":
            answer *= 10
            answer += 9
            check = i
        else:
            check += i

    if check == "zero":
        answer *= 10
    elif check == "one":
        answer *= 10
        answer += 1
    elif check == "two":
        answer *= 10
        answer += 2
    elif check == "three":
        answer *= 10
        answer += 3
    elif check == "four":
        answer *= 10
        answer += 4
    elif check == "five":
        answer *= 10
        answer += 5
    elif check == "six":
        answer *= 10
        answer += 6
    elif check == "seven":
        answer *= 10
        answer += 7
    elif check == "eight":
        answer *= 10
        answer += 8
    elif check == "nine":
        answer *= 10
        answer += 9
    return answer
