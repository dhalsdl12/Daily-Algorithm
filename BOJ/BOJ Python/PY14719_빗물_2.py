h, w = map(int, input().split())
block = list(map(int, input().split()))
answer = 0

for i in range(1, w - 1):
    left = max(block[:i])
    right = max(block[i + 1:])

    water = min(left, right)

    if water > block[i]:
        answer += (water - block[i])
    
print(answer)