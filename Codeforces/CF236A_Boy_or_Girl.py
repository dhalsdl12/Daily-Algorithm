string = input()
dic = {}
for s in string:
    if s not in dic:
        dic[s] = 1

if len(dic) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")