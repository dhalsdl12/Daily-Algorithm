import sys


s = sys.stdin.read()
alpha = [0 for _ in range(26)]

for c in s:
    if c.islower():
        alpha[ord(c) - 97] += 1

for i in range(26):
    if alpha[i] == max(alpha):
        print(chr(97+i), end='')
