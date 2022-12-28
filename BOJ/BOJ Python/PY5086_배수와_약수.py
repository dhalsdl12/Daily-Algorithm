word = []
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a % b == 0:
        word.append("multiple")
    elif b % a == 0:
        word.append("factor")
    else:
        word.append("neither")

for i in range(len(word)): print(word[i])