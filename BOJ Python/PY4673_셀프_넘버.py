number = set(range(1,10001))
generate = set()

for i in range(1,10001):
    num = i
    for j in str(i):
        num += int(j)
    generate.add(num)

self_number = sorted(number - generate)

for i in self_number:
    print(i)