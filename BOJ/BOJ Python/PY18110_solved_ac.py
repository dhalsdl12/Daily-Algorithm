import sys

def rround(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


n = int(sys.stdin.readline())

if n == 0:
    print(0)
else:
    arr = []
    for _ in range(n):
        a = int(sys.stdin.readline())
        arr.append(a)
    arr.sort()

    nn = rround(n * 0.15)
    answer = sum(arr[nn : n - nn])
    print(rround(answer / (n - 2 * nn)))
