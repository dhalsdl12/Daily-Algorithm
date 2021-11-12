def op(depth, total, plus, sub, mul, div):
    global mini, maxi
    if depth == n:
        maxi = max(total, maxi)
        mini = min(total, mini)
        return

    if plus:
        op(depth + 1, total + a[depth], plus - 1, sub, mul, div)
    if sub:
        op(depth + 1, total - a[depth], plus, sub - 1, mul, div)
    if mul:
        op(depth + 1, total * a[depth], plus, sub, mul - 1, div)
    if div:
        op(depth + 1, int(total / a[depth]), plus, sub, mul, div - 1)


n = int(input())

a = list(map(int, input().split()))
cal = list(map(int, input().split()))

maxi = -1e9
mini = 1e9

op(1, a[0], cal[0], cal[1], cal[2], cal[3])

print(maxi)
print(mini)