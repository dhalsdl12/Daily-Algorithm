grade = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

number = 0
answer = 0

for _ in range(20):
    n, s, g = input().split()
    s = float(s)

    if g != 'P':
        number += s
        answer += (s * score[grade.index(g)])

print('%.6f' % (answer / number))