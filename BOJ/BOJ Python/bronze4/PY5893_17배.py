from collections import deque

num = input()
n = len(num)
number = 0
for i in range(n):
    number += (2 ** (n - i - 1)) * int(num[i])

number *= 17

arr = deque()
while True:
    a = number % 2
    arr.appendleft(a)
    number //= 2
    if number == 0:
        break

for a in arr:
    print(a, end='')
