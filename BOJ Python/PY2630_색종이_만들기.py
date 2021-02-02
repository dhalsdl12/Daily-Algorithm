num = int(input())
blue, white = 0,0
matrix = []

def quad_tree(x,y,n):
    global matrix, blue, white
    double_break = False
    color = matrix[x][y]

    for i in range(x, x+n):
        if double_break == True:
            break
        for j in range(y, y+n):
            if matrix[i][j] != color:
                quad_tree(x,y,n//2)
                quad_tree(x+n//2, y, n//2)
                quad_tree(x, y+n//2, n//2)
                quad_tree(x+n//2, y+n//2, n//2)
                double_break = True
                break
    if double_break == False:
        if matrix[x][y] == 1:
            blue += 1
        else:
            white += 1
for i in range(num):
    matrix.append(list(map(int, input().split())))

quad_tree(0,0,num)

print(white)
print(blue)