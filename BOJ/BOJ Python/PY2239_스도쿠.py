import sys


def Sudoku(num):
    if num == len(blank):
        for sudo in sudoku:
            for su in sudo:
                print(su, end='')
            print()
        exit(0)

    x_blank, y_blank = blank[num]
    for i in range(1, 10):
        if check_RowColRect(x_blank, y_blank, i):
            sudoku[x_blank][y_blank] = i
            Sudoku(num + 1)
            sudoku[x_blank][y_blank] = 0


def check_RowColRect(x, y, number):
    x_rect = (x // 3) * 3
    y_rect = (y // 3) * 3
    for i in range(9):
        if number == sudoku[x][i]:
            return False
        if number == sudoku[i][y]:
            return False
        if number == sudoku[x_rect + (i // 3)][y_rect + (i % 3)]:
            return False
    return True


sudoku, blank = [], []

for i in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().rstrip())))
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append((i, j))

Sudoku(0)
