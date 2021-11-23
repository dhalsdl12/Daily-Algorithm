inday = list(map(int, input().split()))
outday = list(map(int, input().split()))
sum = 0

if outday[2] - inday[2] < 0:
    outday[1] -= 1
    outday[2] += 30

if outday[1] - inday[1] < 0:
    outday[0] -= 1
    outday[1] += 12

year = outday[0] - inday[0]
yeargap = 0
yearcnt = 1
yvac = 0

month = outday[1] - inday[1] + (outday[0] - inday[0]) * 12
monthcnt = 0
mvac = 0

sum += (outday[0] - inday[0]) * 12 * 30
sum += (outday[1] - inday[1]) * 30
sum += (outday[2] - inday[2])

while True:
    yvac += (15 + yeargap)
    if yearcnt % 2 == 0:
        yeargap += 1
    yearcnt += 1
    year -= 1
    if year == 0:
        break

while True:
    mvac += 1
    monthcnt += 1
    if monthcnt == 36:
        break
    if monthcnt == month:
        break

print(yvac, end=" ")
print(mvac)
print(sum, end="")
print("days")
