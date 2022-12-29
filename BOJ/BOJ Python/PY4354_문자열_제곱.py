def shorthead(sentence):
    x = len(sentence)
    for i in range(1, (x // 2)+1):
        if x % i == 0:
            s = sentence[0:i]
            count = int(x / i)
            if s * count == sentence:
                #return '('+s+')'+'_'+str(count)
                return count
    #return sentence
    return 1


while True:
    a = input()
    if a == ".":
        break
    print(shorthead(a))