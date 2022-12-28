aaa = input()
result = []
i = 0
check = 0
check2 = 0
first = 0
second = 0
cal = ''
calcheck = 0
while True:
    if i == len(aaa):
        break
    elif aaa[i] == 'Z':
        if aaa[i + 1:i + 4] == "ERO":
            result.append(str(0))
            if check == 0:
                first *= 10
                first += 0
            elif check == 1:
                second *= 10
                second += 0
            i += 4
        else:
            check2 = 1
            break
    elif aaa[i] == 'O':
        if aaa[i + 1:i + 3] == "NE":
            result.append(str(1))
            if check == 0:
                first *= 10
                first += 1
            elif check == 1:
                second *= 10
                second += 1
            i += 3
        else:
            check2 = 1
            break
    elif aaa[i] == 'T':
        if aaa[i + 1:i + 3] == "WO":
            result.append(str(2))
            if check == 0:
                first *= 10
                first += 2
            elif check == 1:
                second *= 10
                second += 2
            i += 3
        elif aaa[i + 1:i + 5] == "HREE":
            result.append(str(3))
            if check == 0:
                first *= 10
                first += 3
            elif check == 1:
                second *= 10
                second += 3
            i += 5
        else:
            check2 = 1
            break
    elif aaa[i] == 'F':
        if aaa[i + 1:i + 4] == "OUR":
            result.append(str(4))
            if check == 0:
                first *= 10
                first += 4
            elif check == 1:
                second *= 10
                second += 4
            i += 4
        elif aaa[i + 1:i + 4] == "IVE":
            result.append(str(5))
            if check == 0:
                first *= 10
                first += 5
            elif check == 1:
                second *= 10
                second += 5
            i += 4
        else:
            check2 = 1
            break
    elif aaa[i] == 'S':
        if aaa[i + 1:i + 3] == "IX":
            result.append(str(6))
            if check == 0:
                first *= 10
                first += 6
            elif check == 1:
                second *= 10
                second += 6
            i += 3
        elif aaa[i + 1:i + 5] == "EVEN":
            result.append(str(7))
            if check == 0:
                first *= 10
                first += 7
            elif check == 1:
                second *= 10
                second += 7
            i += 5
        else:
            check2 = 1
            break
    elif aaa[i] == 'E':
        if aaa[i + 1:i + 5] == "IGHT":
            result.append(str(8))
            if check == 0:
                first *= 10
                first += 8
            elif check == 1:
                second *= 10
                second += 8
            i += 5
        else:
            check2 = 1
            break
    elif aaa[i] == 'N':
        if aaa[i + 1:i + 4] == "INE":
            result.append(str(9))
            if check == 0:
                first *= 10
                first += 9
            elif check == 1:
                second *= 10
                second += 9
            i += 4
        else:
            check2 = 1
            break
    elif aaa[i] == '+' or aaa[i] == '-' or aaa[i] == 'x' or aaa[i] == '/' or aaa[i] == '=':
        if cal == '+':
            first += second
        elif cal == '-':
            first -= second
        elif cal == 'x':
            first *= second
        elif cal == '/':
            first //= second

        if aaa[i] == '=':
            if calcheck == 0:
                check2 = 1
                break
        result.append(aaa[i])
        cal = aaa[i]
        calcheck = 1
        second = 0
        i += 1
        check = 1
    else:
        check2 = 1
        break
if check2 == 1:
    print("Madness!")
else:
    check = 0
    for i in range(len(result)):
        print(result[i], end="")
    print()
    strfirst = str(first)
    answer = ''
    for i in strfirst:
        if i == '-':
            answer += '-'
        elif i == '1':
            answer += "ONE"
        elif i == '2':
            answer += "TWO"
        elif i == '3':
            answer += "THREE"
        elif i == '4':
            answer += "FOUR"
        elif i == '5':
            answer += "FIVE"
        elif i == '6':
            answer += "SIX"
        elif i == '7':
            answer += "SEVEN"
        elif i == '8':
            answer += "EIGHT"
        elif i == '9':
            answer += "NINE"
        elif i == '0':
            answer += "ZERO"
    print(answer)
