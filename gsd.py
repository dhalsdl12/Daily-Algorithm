def cal(num, now_l, now_r, pos, handed):
    l, r = 0, 1
    dis_l = abs(pos[now_l][l] - pos[num][l]) + abs(pos[now_l][r] - pos[num][r])
    dis_r = abs(pos[now_r][l] - pos[num][l]) + abs(pos[now_r][r] - pos[num][r])

    if dis_l == dis_r:
        return 'R' if handed == 'right' else 'L'
    return 'R' if dis_r < dis_l else 'L'


def solution(numbers, hand):
    result = ''
    position = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                4: (1, 0), 5: (1, 1), 6: (1, 2),
                7: (2, 0), 8: (2, 1), 9: (2, 2),
                '*': (3, 0), 0: (3, 1), '#': (3, 2)}

    left = {1, 4, 7}
    right = {3, 6, 9}

    now_l = '*'
    now_r = '#'

    for num in numbers:
        if num in left:
            result += 'L'
            now_l = num
        elif num in right:
            result += 'R'
            now_r = num
        else:
            result += cal(num, now_l, now_r, position, hand)
            if result[-1] == 'L':
                now_l = num
            else:
                now_r = num
    return result
