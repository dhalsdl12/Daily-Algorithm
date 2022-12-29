import math
import sys
n1, n2 = map(int, sys.stdin.readline().split())

ans = math.factorial(n1)//(math.factorial(n2)*math.factorial(n1-n2))
print(ans%10007)