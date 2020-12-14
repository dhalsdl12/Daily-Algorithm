word = input()

cro = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for i in range(len(cro)):
    word = word.replace(cro[i], 'a')

print(len(word))