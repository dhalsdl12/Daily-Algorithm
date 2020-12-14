a = input()
b = input()
c = input()

num = int(a)*int(b)*int(c)

num = str(num)

for i in range(0, 10):
    print(num.count(str(i)))