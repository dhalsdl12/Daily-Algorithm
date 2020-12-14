word = input().strip()

if len(word) == 0:
    print("0")
else:
    print(word.count(' ')+1)