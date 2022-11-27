def quad_tree(x,y,n):
    global matrix, minus, zero, one
    double_break = False
    number = matrix[x][y]

    for i in range(x, x+n):
        if double_break == True:
            break
        for j in range(y, y+n):
            if matrix[i][j] != number:
                quad_tree(x,y,n//3)
                quad_tree(x, y+n//3, n//3)
                quad_tree(x, y+2*n//3, n//3)
                quad_tree(x+n//3, y, n//3)
                quad_tree(x+n//3, y+n//3, n//3)
                quad_tree(x+n//3, y+2*n//3, n//3)
                quad_tree(x+2*n//3, y, n//3)
                quad_tree(x+2*n//3, y+n//3, n//3)
                quad_tree(x+2*n//3, y+2*n//3, n//3)
                double_break = True
                break
    if double_break == False:
        if matrix[x][y] == -1:
            minus += 1
        elif matrix[x][y] == 0:
            zero += 1
        else:
            one += 1

num = int(input())
matrix = []
minus = 0
zero = 0
one = 0

for i in range(num):
    matrix.append(list(map(int, input().split())))
quad_tree(0,0,num)
print(minus)
print(zero)
print(one)