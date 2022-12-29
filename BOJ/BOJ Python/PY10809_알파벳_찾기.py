word = input()

for i in 'abcdefghijklmnopqrstuvwxyz':
    try:
        print(word.index(i), end=' ')
    except:
        print(-1, end=' ')