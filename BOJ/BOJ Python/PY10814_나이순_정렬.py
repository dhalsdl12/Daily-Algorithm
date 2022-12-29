import sys

num = int(sys.stdin.readline())
client = []

for i in range(num):
    age, name = input().split()
    client.append((age, name))

client.sort(key = lambda x: int(x[0]))

for cl in client:
    print(cl[0], cl[1])