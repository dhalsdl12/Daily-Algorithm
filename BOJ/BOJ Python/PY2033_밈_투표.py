n = int(input())

li = ['Never gonna give you up',
    'Never gonna let you down',
    'Never gonna run around and desert you',
    'Never gonna make you cry',
    'Never gonna say goodbye',
    'Never gonna tell a lie and hurt you',
    'Never gonna stop']

answer = 0
for i in range(n):
    s = input()

    if s not in li:
        answer = 1

if answer == 0:
    print('No')
else:
    print('Yes')