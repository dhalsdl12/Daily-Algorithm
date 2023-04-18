n = int(input())
string = input()
m = ['a', 'e', 'u', 'i', 'o']
answer = 0

for i in range(n):
    if string[i] in m:
        answer += 1

print(answer)