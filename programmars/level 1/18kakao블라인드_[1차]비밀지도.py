def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        str1 = ''
        for j in range(n):
            if arr1[i] % 2 == 1:
                tmp = '#'
            else:
                if arr2[i] % 2 == 1:
                    tmp = '#'
                else:
                    tmp = ' '
            arr1[i] //= 2
            arr2[i] //= 2
            str1 = tmp + str1
        answer.append(str1)
    return answer