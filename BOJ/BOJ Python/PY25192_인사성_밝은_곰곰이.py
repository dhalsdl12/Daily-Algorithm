n = int(input())
dic = {}
count = 0

for _ in range(n):
    string = input()
    if string == 'ENTER':
        dic = {}
    else:
        if string not in dic:
            dic[string] = 1
            count += 1

print(count)