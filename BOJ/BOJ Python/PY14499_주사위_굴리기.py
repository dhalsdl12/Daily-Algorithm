def move(dir):
    if dir == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif dir == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif dir == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    elif dir == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]


def direct(dir):
    if dir == 1:
        return 0, 1
    if dir == 2:
        return 0, -1
    if dir == 3:
        return -1, 0
    if dir == 4:
        return 1, 0
    

n, m, x, y, k = map(int, input().split())
arr = []
answer = []
dice = [0, 0, 0, 0, 0, 0, 0]

for _ in range(n):
    arr.append(list(map(int, input().split())))

command = list(map(int, input().split()))

for c in command:
    dx, dy = direct(c)
    if 0 <= x + dx < n and 0 <= y + dy < m:
        x += dx
        y += dy
        move(c)

        if arr[x][y] != 0:
            dice[1] = arr[x][y]
            arr[x][y] = 0
        else:
            arr[x][y] = dice[1]
        answer.append(dice[6])

for ans in answer:
    print(ans)