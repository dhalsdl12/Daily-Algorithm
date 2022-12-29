import sys

def multi(a, b):
    if(b == 1):
        return a
    if(b == 0):
        return 1
    elif(b%2 == 0):
        return multi(a, b//2)**2%c
    elif(b%2 == 1):
        return (multi(a,b-1))*a

a,b,c = map(int, sys.stdin.readline().split())
print(multi(a, b)%c)