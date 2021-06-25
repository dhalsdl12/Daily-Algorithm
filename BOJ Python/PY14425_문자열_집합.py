import sys

n, m = map(int, sys.stdin.readline().split())
cnt = 0

#딕셔너리 사용
arr = {sys.stdin.readline() for i in range(n)}

for i in range(m):
    string = sys.stdin.readline()

    if string in arr:
        cnt += 1

print(cnt)