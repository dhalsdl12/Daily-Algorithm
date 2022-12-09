a, b = map(int, input().split())
year = 0

while True:
    year += 1
    a *= 3
    b *= 2
    if a > b:
        break
print(year)