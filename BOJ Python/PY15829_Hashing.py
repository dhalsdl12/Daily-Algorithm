r = 31
m = 1234567891

num = int(input())
word = input()
answer = 0

for i in range(num):
    answer += (ord(word[i])-96)*(r**i)
print(answer%m)
