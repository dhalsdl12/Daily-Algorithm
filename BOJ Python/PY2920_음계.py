music = list(map(int, input().split()))
a = 0
if music[0] == 1:
    for i in range(1, len(music)):
        if music[i] > music[i-1]:
            continue
        else:
            print("mixed")
            a = 1
            break
    if a == 0:
        print("ascending")

elif music[0] == 8:
    for i in range(1, len(music)):
        if music[i] < music[i-1]:
            continue
        else:
            print("mixed")
            a = 1
            break
    if a == 0:
        print("descending")
else:
    print("mixed")