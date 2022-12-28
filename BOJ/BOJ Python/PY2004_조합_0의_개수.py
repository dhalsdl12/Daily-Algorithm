import sys
def div_number(num, n):
    count = 0
    while(num!=0):
        num = num//n
        count += num
    return count

n, m = map(int, sys.stdin.readline().split())

div_five = div_number(n,5) - div_number(m,5) - div_number(n-m,5)
div_two = div_number(n,2) - div_number(m,2) - div_number(n-m,2)

print(min(div_five, div_two))