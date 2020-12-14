num = int(input())

for i in range(num):
    number, s = input().split()
    result = ""

    for c in s:
        result += c*int(number)
    print(result)