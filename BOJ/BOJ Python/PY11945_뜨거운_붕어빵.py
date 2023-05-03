n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(input())

for a in arr:
    print(a[::-1])