arr = []
string = ''
for i in range(5):
    a = input()
    arr.append(a + ' ' * (15 - len(a)))

for j in range(15):
    for i in range(5):
        if arr[i][j] != ' ':
            string += arr[i][j]
            
print(string)