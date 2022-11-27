def quad_tree(x,y,n):
    global matrix
    color = matrix[x][y]
    if n==1:
        return str(matrix[x][y])
    result = []
    for i in range(x, x+n):
        for j in range(y, y+n):
            if matrix[i][j] != color:
                result.append('(')
                result.extend(quad_tree(x,y,n//2))
                result.extend(quad_tree(x, y+n//2, n//2))
                result.extend(quad_tree(x+n//2, y, n//2))
                result.extend(quad_tree(x+n//2, y+n//2, n//2))
                result.append(')')
                
                return result
    return str(matrix[x][y])

num = int(input())
matrix = []

for i in range(num):
    matrix.append(list(map(int, input())))
print(''.join(quad_tree(0,0,num)))