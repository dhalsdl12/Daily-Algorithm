import sys

num = int(sys.stdin.readline())
char = []
sorted_char = []

for i in range(num):
    char.append(input())

char = set(char)
for i in char:
    sorted_char.append((len(i),i))

sorted_char.sort()

for word_len, word in sorted_char:
    print(word)