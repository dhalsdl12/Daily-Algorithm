num = int(input())
bag = 0

while num > 0:
    if num %5 == 0:
        num -= 5
        bag += 1
    
    elif num%3 == 0:
        num -= 3
        bag += 1
    
    elif num > 5:
        num -= 5
        bag += 1

    else:
        bag = -1
        break

print(bag)    