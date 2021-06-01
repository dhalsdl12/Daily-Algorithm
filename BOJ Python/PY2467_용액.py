import sys

num = int(input())

a = list(map(int, input().split()))
a.sort()
MIN = sys.maxsize
left = 0
right = num - 1
aL = 0
aR = 0

while left < right:
    Sum = a[left] + a[right]

    if abs(Sum) < MIN:
        aL = left
        aR = right
        MIN = abs(Sum)
    if Sum > 0:
        right -= 1
    elif Sum < 0:
        left += 1
    else:
        break

print(a[aL], a[aR])