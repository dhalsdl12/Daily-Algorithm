input_a = input().split()

a = int(input_a[0])
b = int(input_a[1])

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")