word = input().upper()

dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time = 0

for i in range(len(word)):
    for s in dial:
        if word[i] in s:
            time += dial.index(s)+3

print(time)