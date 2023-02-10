a, b = map(int, input().split())
n, m = map(int, input().split())

robots = []
command = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(n):
    x, y, z = input().split()
    if z == 'N':
        d = 0
    if z == 'E':
        d = 1
    if z == 'S':
        d = 2
    if z == 'W':
        d = 3
    robots.append([int(x), int(y), d])

for _ in range(m):
    x, y, z = input().split()
    command.append([int(x), y, int(z)])

for r, c, repeat in command:
    for _ in range(repeat):
        if c == 'F':
            direction = robots[r - 1][2]
            robots[r - 1][0] += dx[direction]
            robots[r - 1][1] += dy[direction]
            
            if robots[r - 1][0] > a or robots[r - 1][1] > b or robots[r - 1][0] <= 0 or robots[r - 1][1] <= 0:
                print(f'Robot {r} crashes into the wall')
                exit(0)
            for j in range(n):
                if j != r - 1:
                    if robots[r - 1][0] == robots[j][0] and robots[r - 1][1] == robots[j][1]:
                        print(f'Robot {r} crashes into robot {j + 1}')
                        exit(0)
        if c == 'L':
            robots[r - 1][2] = (robots[r - 1][2] - 1) % 4
        if c == 'R':
            robots[r - 1][2] = (robots[r - 1][2] + 1) % 4
    
print('OK')