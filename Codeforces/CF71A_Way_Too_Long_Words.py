n = int(input())
answer = []
words = [input() for i in range(n)]
for word in words:
    if len(word) > 10:
        word = word[0] + str(len(word) - 2) + word[-1]
    answer.append(word)
for ans in answer:
    print(ans)
