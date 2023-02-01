import sys

s1 = list(sys.stdin.readline().strip())
s2 = []

n = int(sys.stdin.readline())

for i in range(n):
    cursor = len(s1)
    st = sys.stdin.readline().strip()
    if st[0] == "L":
        if cursor == 0:
            continue
        else:
            s2.append(s1.pop())
    elif st[0] == "D":
        if len(s2) == 0:
            continue
        else:
            s1.append(s2.pop())
    elif st[0] == "B":
        if cursor == 0:
            continue
        else:
            s1.pop()
    elif st[0] == "P":
        s1.append(st[2])

print("".join(s1 + list(reversed(s2))))
