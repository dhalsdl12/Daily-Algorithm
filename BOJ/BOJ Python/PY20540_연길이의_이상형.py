s = input()
arr = ['E','I','S','N','T','F','J','P']

for c in s:
    arr.remove(c)

print(''.join(arr))