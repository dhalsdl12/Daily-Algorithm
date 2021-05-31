import math
def a(shift):
    c = len(s)
    for i in range(c):
        s.append(s[i] + s[i])
        s[i] = ("   "*shift + s[i] + "   "*shift)


s = ['  *   ',' * *  ','***** ']
num = int(input())
k = int(math.log(int(num/3), 2))
for i in range(k):
    a(int(pow(2,i)))
for i in range(num):
    print(s[i])